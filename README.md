# Customer Service Web Application using PySpark for Big Data Processing
Part of the Udacity Data Science Nanodegree: __Spark Project: Sparkify__.

## General info
A __web app__ created with Flask and Bootstrap provides key customer metrics. The target audience are customer support agents of the fictional music streaming company _Sparkify_. The app provides an __interface__ to filter for a specific customer.

Apache __Spark__ as a _technology for distributed data processing_ is used to cope with __Big Data__.

To predict __Churn__ we apply Machine Learning algorithms to 12 GB of logfile data. While Big Data has no universal definition we consider the problem to fall into this domain as it cannot be solved without a __network of distributed computers__.

__New training data__ can be provided and used to update the churn prediction model. A manual __ETL and Machine Learning (ML) pipeline__ is provided: A Jupyter notebook contains all the code for data cleaning, training the classifier and providing the best model to the web app. Manual pipelines as the code is not transferred to a .py file to execute programmatically.

## Requirements
_Web app_: Python 3 mainly with the packages Pandas, flask, plotly, and sqlalchemy.

_PySpark_: The input dataset is logfile data. The processing result is the aggregated customer information in a SQLite database. The processing uses PySpark, a _Python interface for Apache Spark_. Amazon Web Services Elastic Map Reduce, in short __AWS EMR__ is a possible infrastructure choice for the processing.

## Instructions
To run the web app:
- Execute the Python file 'run.py' in the 'app' folder via the command line:
    `python run.py`
- Go to http://0.0.0.0:3001/ in a browser.

To run the PySpark notebook (see 'files' below):
- Bring the pyspark Jupyter notebook to infrastructure able to execute PySpark code.
- An AWS S3 link to the dataset used can be found in the notebook, section `Gather data`.
- The `sparkify.db` saved when running the code is expected by the web app in the folder `data`.

## Files:
Folder `analysis` contains the Jupyter notebook for the PySpark Churn analysis.

`data` contains the PySpark job output `sparkify.db`, an SQLite database.

`sparkify_app` contains the web application.

## Discussion of approach
For the Churn analysis please refer to the Jupyter notebook in `analysis`. To reduce the runtime only two algorithms and a subset of the data is considered.

The Sparkify app gives an overview when a customer service agent starts the application. When handling a customer issue he finds customer specific information, including the customers __likelihood to cancel the service__ (churn), by entering the customer number.

The customer number is assumed to be known e.g. from a CRM tool. The app helps best when integrated in such a solution.
