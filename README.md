# SQLalchemy-Challenge
An exercise demonstrating some of the features of SQLalchemy.

## Overview:
	SQLalchemy is a tool that allows users to build on their SQL skills and integrate their knowledge of python while working with SQL databases. We will also look at the Flask tool, which will allow us to create api references, where the user will be able to access our queries from a server. We know that SQL databases house data for an organization and provide an opportunity to store a large amount of data and develop various queries to understand the data better. This exercise will use SQLalchemy to access data from an SQLite database and import the data into a jupyter notebook. In the notebook, we will be able to use SQLalchemy to merge our SQL and Python skills to develop various queries to discover key insights about the data. Ultimately, our goal in developing queries should be to allow the user to make the decisions necessary based on their data efficiently. As usual, once we understand the customer's needs, we should take a moment to explore the data and better understand its design and potential limitations.
	We begin by creating accessing the SQLite database using SQLaclhemy. We can then create a reflection of the database, allowing us to access the data better and create a session that will enable us to access the data in each table within the database. This portion of the exercise is similar to creating the schema of the database in SQL.
	Once all of our data connections are ready, we can begin scripting our queries. SQLalchemy allows us to write queries with a similar syntax to that of SQL. However, you will notice that we now have additional capabilities due to our additional python functionality. We can now further analyze the data using pandas and matplotlib. You will notice that this increased functionality is important for analyzing the data in several ways within the same platform. 
	We can utilize the SQLalchemy syntax to create queries for the hawaii database and analyze the data from the Measurements and Station table. Whereas we would normally use our SQL environment to conduct the connections and to filter for each table within the database, we will find that we can produce the same results using the SQLalchemy tools. This dramatically improves our ability to analyze data in a way that would not have been as easy to do when all the data would be solely in an SQL environment. 
	Using the Flask tool, we can then create an app that allows the user to reference our queries from a server using a browser. This provides a fast and efficient means of sharing the results of our analysis with a user and can be a more user-friendly way of digesting the information. The Flask functionality is accessed using the VScode environment. However, the syntax for our queries remains the same as we did in our jupyter notebook. You will notice that this makes it relatively easy to reproduce the queries for consumption using the Flask app that we create as we jsonify our output, which makes it much easier for the user to read and comprehend. 

### Part 1: Climate Analysis and Exploration

In this section, you’ll use Python and SQLAlchemy to perform basic climate analysis and data exploration of your climate database. Complete the following tasks by using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use the provided [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to complete your climate analysis and data exploration.

* Use SQLAlchemy’s `create_engine` to connect to your SQLite database.

* Use SQLAlchemy’s `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

* Link Python to the database by creating a SQLAlchemy session.

* **Important:** Don't forget to close out your session at the end of your notebook.

#### Precipitation Analysis

To perform an analysis of precipitation in the area, do the following:

* Find the most recent date in the dataset.

* Using this date, retrieve the previous 12 months of precipitation data by querying the 12 previous months of data. **Note:** Do not pass in the date as a variable to your query.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame, and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results by using the DataFrame `plot` method

* Use Pandas to print the summary statistics for the precipitation data.

#### Station Analysis

To perform an analysis of stations in the area, do the following:

* Design a query to calculate the total number of stations in the dataset.

* Design a query to find the most active stations (the stations with the most rows).

    * List the stations and observation counts in descending order.

    * Which station id has the highest number of observations?

    * Using the most active station id, calculate the lowest, highest, and average temperatures.

    * **Hint:** You will need to use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

* Design a query to retrieve the previous 12 months of temperature observation data (TOBS).

    * Filter by the station with the highest number of observations.

    * Query the previous 12 months of temperature observation data for this station.

    * Plot the results as a histogram with `bins=12`

* Close out your session.

### Part 2: Design Your Climate App

Now that you have completed your initial analysis, you’ll design a Flask API based on the queries that you have just developed.

Use Flask to create your routes, as follows:

* `/`

    * Homepage.

    * List all available routes.

* `/api/v1.0/precipitation`

    * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

    * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

    * Query the dates and temperature observations of the most active station for the previous year of data.

    * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than or equal to the start date.

    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates from the start date through the end date (inclusive).

