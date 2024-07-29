# Data Engineer Technical Assessment


The purpose of this technical assessment is to assess your familiarity with the technologies we use here at Plaid. Please read all the instructions carefully. This exercise should take roughly 1-2 hours to complete, but may take longer if you're unfamiliar with [dbt](https://www.getdbt.com/docs/) or need to install additional dependencies locally.


## Setup Instructions & Deliverables

During your development, make sure to append the `--profiles-dir .` option when running any `dbt` commands so that the provided `profiles.yml` file is used. Not all the tables in the database are needed for the deliverables.

The `dbt run` and `dbt test` commands should execute successfully on a completed project. If you're unfamiliar with dbt, check out the documentation [here](https://docs.getdbt.com/).

Provided for you is a seed database of some sample airline flights and bookings. You can find an overview [here](https://postgrespro.com/docs/postgrespro/12/demodb-bookings). You can also find schema descriptions and some background information to help yourself familiarize with the objects.

1. Setup the necessary packages and virtual environment. It is advised that you work on this assessment from a newly created virtual environment.
   - If not already installed, install [Docker Desktop](https://docs.docker.com/get-docker/)
   - If not already installed, install [dbt-postgres](https://docs.getdbt.com/dbt-cli/install/overview)

2. Build database image

```sh
docker build --tag plaid-assessment .
```

3. Start database

```sh
docker run --name plaid-assessment --detach --publish 5438:5432 plaid-assessment
```

1. Verify the database is accessible at `postgresql://postgres:plaid@localhost:5438/postgres`. You can use the command line, or any SQL workbench of your choice. You will be asked to share your screen and pull up the tool of your choice, as well as your IDE so we can modify your models as needed while having the technical discussion.


2. Build a data model to answer the following questions. You can create as many tables as you'd like, as long as the following requirements are satisfied. Give the tables a reasonable name, and put them in the `models` folder. You might encounter questions you are unsure about. Keep note of them and use your best effort. We will discuss them during the discussion portion of the interview. You are not expected to get 100% right.
    - Aggregates on total ticket sales with the following metrics:
        - Total number of tickets in daily, rolling 7 and 28 days
    - Number of redemption bookings by day
        - Redemption bookings, in layman terms, are free tickets that customers could redeem, for example with points.
        - Airlines typically would mark a booking as a redemption by substituting in dummy values in the cost field to indicate as such. It would be helpful to examine the shape of the data in the table and decide how you'd want to handle this in your model. Different airlines might use different dummy values!
    - Table showing all valid and bookable routes.
        - Valid routes are defined by flights that can be completed within 24 hours, with a maximum of 1 transfer. A bookable route cannot start and end at the same airport.
        - This table should include the following:
          - Origin airport code and departure time
          - Destination airport code and and arrival time
          - Transfer airport code, if any, departure time, and arrival time
          - Flight numbers of each flight
        - Use `bookings.routes` instead of `bookings.flights` for your model, as `bookings.flights` is a fact table containing historical information.
        
3. To save space, before submitting your answers please delete `database/0_migrate.sql`. Make sure you've committed all your changes, then generate a zip of the local branch and send it to the interviewer:
```sh
git archive HEAD -o lastname_firstname.zip
```

Please make sure to keep your Docker container and other tools you have used for this interview available as you will be asked to show your development environment during the discussion portion with the interviewer.