

# Customer service web application based on Pyspark Big Data Processing
Part of the Udacity Data Science Nanodegree, the __Spark Project: Sparkify__.

## General info
A __web app__ created with Flask and Bootstrap provides key customer metrics for customer support personnel of the fictional music streaming company 'Sparkify'. The app provides an __interface__ to filter for a specific customer.

Apache __Spark__ as a _technology for distributed data processing_ is used to cope with __Big Data__.

To predict __Churn__ we apply Machine Learning algorithms to 12 GB of logfile data. While Big Data has no universal definition we consider the problem to fall into this domain as it cannot be solved without a _network of distributed computers_.

_Open: refer to other project for the following possibilities:_:
__New training data__ can be provided and used to update the model. More precisely, data cleaning and storing in a database can be performed using an __ETL pipeline__, and training the classifier and providing the best model to the web app can be performed using a __Machine Learning (ML) pipeline__.

## Requirements
_Web app_: Python 3 mainly with the packages Pandas, flask, plotly, and sqlalchemy.

_PySpark_: The input dataset is logfile data. The processing result is the aggregated customer information in a SQLite database. The processing uses PySpark, a _Python interface for Apache Spark_. Amazon Web Services Elastic Map Reduce, in short __AWS EMR__ is a possible infrastructure choice for the processing.

## Instructions
To run the web app:
- Execute the Python file 'run.py' in the 'app' folder via the command line:
    `python run.py`
- Go to http://0.0.0.0:3001/ in a browser.

_Open: implement or skip:_
To run the pipelines:
- Run the ETL pipeline via the command line in the `data` folder:<br>
        `python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db`
- Run the ML pipeline via the command line in the `models` folder. The best model and its score are printed:<br>
        `python train_classifier.py ../data/DisasterResponse.db disaster_model.pkl`

## Files -- TODO: continue readme update here
Folder `notebooks_code_development` contains Jupyter notebooks used to develop the pipelines.

`data` contains the ETL pipeline (`process_data.py`) and the CSV input files plus the ETL pipeline output, an SQLite database.

`models` contains the ML pipeline (`train_classifier.py`) with its output, i.e. a Python pickle file with the best model from testing different classifiers and parameters. That pickle file is used in the app to classify new messages. and a Python pickle file with input for some of the graphs in the app.

`app` contains the web application.

## Discussion of approach
### Imbalanced data
The data is imbalanced. There are few massages in the training data for some of the 36 categories to classify.

__Accuracy not appropriate:__<br>
Hence, we need to take care of how to measure the classification performance. When a category like 'water' appears just 1% of the time we are 99% right to not predict the category 'water' at all. It is the accuracy score giving 99%. Both recall and precision are helpful for imbalanced data. Recall answers how many of the values actually positive are identified correctly? Precision answers how many of the values predicted as positive are identified correctly?

__Maximizing the F2 score:__<br>
Looking for the model with the highest F1 score gives equal weight to maximize both recall and precision. For the disaster response model we want to consider precision but give more weight to recall:

We decide for a __recall-oriented model__ to accept to rather providing e.g. water too often as opposed to not help people who are in need. Thus we use the [F-beta scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html) with a beta of 2, i.e. the F2 score. In this multilabel setting, we choose to maximize the F2 score average over all categories weighted by true instances for each label (`average='weighted'`).

### Machine learning pipeline runtime
The `train_classifier.py` is optimized to not take hours to run. A random sample of 5000 of the labeled messages is used.

You can change that in the Python file –look for `load_data(database_filepath, n_draws=5000)`. Also the number iteration and cross validation runs is set quite low searching for the best model. You can change that in the Python file – look for: ```best_model = search.train_model(X_train, y_train, search='random',
                scoring=scorer, n_iter=3, cv=2, iid=False)```

The F2 score obtained from a test run was .567.
