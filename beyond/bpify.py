from flask import Flask, request, jsonify, Response
from markets import MARKETS
from listingsmanager import ListingsManager
from json import dumps
from validationhelper import (
    check_required_listing_fields_present,
    get_required_listing_fields_missing_message,
    check_listing_fields_valid,
    get_valid_listing_fields_message,
    valid_listing_filters,
    get_valid_listing_filters_message,
    valid_calendar_filters,
    get_valid_calendar_filters_message,
)

listings_manager = None


def create_app():
    app = Flask(__name__)
    global listings_manager
    listings_manager = ListingsManager()
    return app


app = create_app()


@app.route("/test_flask", methods=["GET", "POST"])
def test_flask():
    """Example to show how to use Flask and extract information from the incoming request.
    It is not intended to be the only way to do things with Flask, rather more a way to help you not spend too much time on Flask.

    Ref: http://flask.palletsprojects.com/en/1.1.x/

    Try to make those requests:
    curl "http://localhost:5000/test_flask?first=beyond&last=pricing"
    curl "http://localhost:5000/test_flask" -H "Content-Type: application/json" -X POST -d '{"first":"beyond", "last":"pricing"}'

    """
    # This contains the method used to access the route, such as GET or POST, etc
    method = request.method

    # Query parameters
    # It is a dict like object
    # Ref: https://flask.palletsprojects.com/en/1.1.x/api/?highlight=args#flask.Request.args
    query_params = request.args
    query_params_serialized = ", ".join(f"{k}: {v}" for k, v in query_params.items())

    # Get the data as JSON directly
    # If the mimetype does not indicate JSON (application/json, see is_json), this returns None.
    # Ref: https://flask.palletsprojects.com/en/1.1.x/api/?highlight=get_json#flask.Request.get_json
    data_json = request.get_json()

    return jsonify(
        {
            "method": method,
            "query_params": query_params_serialized,
            "data_json": data_json,
        }
    )


@app.route("/markets")
def markets():
    return jsonify([market.to_dict() for market in MARKETS.get_all()])


@app.route("/listings", methods=["GET", "POST"])
def listings():
    if request.method == "POST":
        data_json = request.get_json()
        if not check_required_listing_fields_present(data_json):
            return Response(
                make_error_msg(
                    "Missing required fields: "
                    + get_required_listing_fields_missing_message()
                ),
                status=400,
            )
        else:
            listing_body = {
                "title": data_json["title"],
                "base_price": data_json["base_price"],
                "currency": data_json["currency"],
                "market": data_json["market"],
                "host_name": data_json["host_name"]
                if "host_name" in data_json
                else None,
                "listing_id": listings_manager.get_max_listing_id(),
            }
            listings_manager.create_listing(listing_body)
            return jsonify(listing_body)

    elif request.method == "GET":
        query_params = request.args
        if valid_listing_filters(query_params):
            return jsonify(listings_manager.get_filtered_listings(query_params))
        else:
            return Response(
                make_error_msg(
                    "Invalid filters, valid filters are: "
                    + get_valid_listing_filters_message()
                ),
                status=400,
            )


@app.route("/listings/<int:id>", methods=["GET", "PUT", "DELETE"])
def listing(id):
    cur_listing = listings_manager.get_listing(id)
    if not cur_listing:
        return Response(
            make_error_msg("listing with given id does not exist"), status=404
        )
    else:
        if request.method == "GET":
            return jsonify(cur_listing)
        elif request.method == "PUT":
            data_json = request.get_json()
            if check_listing_fields_valid(data_json):
                listings_manager.update_listing(id, data_json)
                return jsonify(listings_manager.get_listing(id))
            else:
                return Response(
                    make_error_msg(
                        "Invalid field found in request, valid fields are: "
                        + get_valid_listing_fields_message()
                    ),
                    status=400,
                )
        elif request.method == "DELETE":
            listings_manager.delete_listing(id)
            return Response(status=200)


@app.route("/listings/<int:id>/calendar", methods=["GET"])
def listing_calendar(id):
    cur_listing = listings_manager.get_listing(id)
    if not cur_listing:
        return Response(
            make_error_msg("listing with given id does not exist"), status=404
        )
    else:
        query_params = request.args
        if valid_calendar_filters(query_params):
            return jsonify(listings_manager.build_calendar(id, query_params))
        else:
            return Response(
                make_error_msg(
                    "Invalid filters, valid filters are: "
                    + get_valid_calendar_filters_message()
                ),
                status=400,
            )


def make_error_msg(msg):
    return dumps({"message": msg})


if __name__ == "__main__":
    app.run()
