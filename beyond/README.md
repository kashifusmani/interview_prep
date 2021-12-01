BPify: a simplified Beyond Pricing API 


## Table of contents

1. [Intro](#intro)
1. [Your tasks](#your-tasks)
1. [Project Layout](#project-layout)
1. [Running the project](#running-the-project)
1. [Specifications](#specifications)
1. [Submitting](#submitting)
1. [Evaluation](#evaluation)


## Intro

Your mission is to build a simplified API to power the [Beyond Pricing](http://beyondpricing.com) website.

The core concept of Beyond Pricing is a `Listing` - for example, an apartment on Airbnb or HomeAway.

The `Listing` entity carries a certain number of information about the property (title, market, etc) and has a `Calendar` to carry prices and availability. 

A `Calendar` is just a list of dates with added information about each date - for example each date can have a different price:
```
date=2020-01-01, price=500
date=2020-01-02, price=450
```

Additionally, in Beyond Pricing, we have the concept of a "Base Price". When we predict a price for a day, we think of it as a multiple of the base price. E.g. a price of $150 for a specific day is a 1.5x multiple on the base price of $100.

The challenge will work with a simplified version of the listing and the calendar.


## Your tasks

Endpoints to implement:

(See [Specifications](#specifications) for more details)

 1. Create a listing
   <br>See `POST /listings` endpoint
 
 1. Retrieve a listing
   <br>See `GET /listings/:id` endpoint
 
 1. Update a listing
   <br>See `PUT /listings/:id` endpoint

 1. Delete a listing
   <br>See `DELETE /listings/:id` endpoint
 
 1. Retrieve several listings
   <br>See `GET /listings` endpoint

 1. Retrieve a listing's calendar
   <br>See `GET /listings/:id/calendar` endpoint
 

## Project Layout

- We've set up [Flask][flask] in `bpify.py`.
Implement the endpoints in this file. We also added an example to show how to use Flask to process the information of a request.

- We use [black][black] to format the code automatically and focus on what matters instead. We encourage you to use it as well and to run it on your entire codebase: (`black .`).

        
## Running the project

To run the project, open it up in your terminal and run:

```
pip install -r requirements.txt
env FLASK_APP=bpify.py flask run -p 5000
```

Test it is working by running the following in another terminal:

```
curl http://localhost:5000/markets
```

You should see a list of markets.


## Specifications

Your solution **must use python 3.7 or greater**.

Your solution **must persist data into a file** without using an ORM library or a DB system.

Your solution **must use [open exchange rates][open-exchange-rates]** to get the exchange rates. The free plan is enough to complete this task.

The response format of your API **must be JSON** and a proper use of HTTP status codes and error handling is expected.

1. `POST /listings` endpoint

   - Send JSON data in the body, for example:
      ```
      {
         "title": "Comfortable Room In Cozy Neighborhood",
         "base_price": 867,
         "currency": "USD",
         "market": "san-francisco",
         "host_name": "John Smith"
      },
      ```
      All fields are required except for `host_name`.

   - Return: the listing information (including its ID) in a JSON format.

1. `GET /listings/:id` endpoint

   - Return: the listing information (including its ID) in a JSON format.
 
1. `PUT /listings/:id` endpoint
   
   - Send JSON data in the body
   - Update only the fields present in the request
   - Return: the listing information (including its ID) in a JSON format.

1. `DELETE /listings/:id` endpoint

   - A successful response must mean a listing was deleted.

1. `GET /listings` endpoint
   
   - Return: a list of listings in a JSON format.

   - This endpoint should allow to filter by market and base price/currency.

      Those filters must be implemented as query parameters: 

      - `market` - optional
         - A single market or a list of markets separated by commas. It uses the market codes.
         - E.g.: `?market=paris` or `?market=paris,san-francisco`
      
      - `base_price.[e|gt|gte|lt|lte]` - optional
         - The comparison type is part of the query parameter.
         - E.g.: `?base_price.gt=500` or `?base_price.lte=300`

      - `currency` - optional but required when base price is specified
         - It uses the currency codes.
         - E.g.: `?currency=usd`


1. `GET /listings/:id/calendar` endpoint

   - This endpoint returns the listing's calendar (365 days starting from today).
  
   - It must allow to return the calendar in any currency. The default being the listing's currency.
   
      This parameter must be implemented as a query parameter:

      - `currency` - optional
         - It uses the currency codes.
         - E.g.: `?currency=usd`

   - Format for dates: `YYYY-MM-DD`
   - Calendar rules:
        - For the Paris and Lisbon markets: Saturday and Sunday => 1.5x of base price
        - For the San Francisco market: Wednesday => 0.70x of base price
        - For the rest of the markets: Friday => 1.25x of base price
   - Example of response:  
   ```
   [
      {
         "date": "2019-01-01",
         "price": 500,
         "currency": "USD",
      },
      {
         "date": "2019-01-02",
         "price": 550,
         "currency": "USD",
      },
      ...
   ]
   ```


## Submitting

1. Make sure all your changes are committed to `git`.

   ```bash
   $ git status
   On branch master
   nothing to commit, working directory clean
   ```

1. Create a zip archive of your project named `"code-challenge-bpify-[YOUR NAME].zip"`. Make sure to include the .git folder as well.

1. Email us `code-challenge-bpify-[YOUR NAME].zip`.


## Evaluation

Your work will be evaluated based on the following criteria:

 * Correctness: The features you implement work correctly.
   There are no errors in the console. It's not easy to make your code break.
 * Completeness: Every feature is implemented.
 * Cleanliness and ease of use: Your code is easy to understand and extend.
 * Proper use of HTTP status codes
 * Proper error handling

:exclamation: **Important:** Your app **MUST** start successfully.

Please note that we are looking for a straightforward solution, do not spend too much time on this.

If you're unfamiliar with python, check out these few tips:

   * once you have a working python environment, run `pip install PACKAGE_NAME` to install a new package. E.g. `pip install ipython` - Also check the `requirements.txt` file.
   * [ipython][ipython] - IPython is an interactive shell for the Python programming language that offers enhanced introspection, additional shell syntax, tab completion and rich history.
   * [requests][requests] - Requests is an elegant and simple HTTP library for Python, built for human beings.   



[flask]: https://flask.palletsprojects.com/en/1.1.x/
[open-exchange-rates]: https://openexchangerates.org/
[black]: https://github.com/psf/black
[ipython]: https://pypi.org/project/ipython/
[requests]: https://requests.readthedocs.io/en/master/
