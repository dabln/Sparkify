import pandas as pd
import plotly.graph_objs as go
import joblib

def return_graphs(df):
    """Creates four plotly visualizations
    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """

    # extract data for visuals
    gender_count = df.groupby('gender').count().userId
    gender_names = list(gender_count.index)
    hovertext = 'UserId ' + df.userId.apply(str)
    #scatter = joblib.load("../data/scatter_data.pkl")

    # creating the visuals
    graph_one = []
    graph_one.append(
      go.Bar(
      x = gender_names,
      y = gender_count
      )
    )
    layout_one = dict(title = 'Distribution of Message Categories',
                xaxis = dict(title = 'Category'),
                yaxis = dict(title = 'Count'),
                )

    graph_two = []
    graph_two.append(
        go.Scatter(x=df.songs_per_day, y=df.days_listened, mode='markers', hovertext=hovertext)
    )
    layout_two = dict(title = 'Days vs. Songs Listened',
                xaxis = dict(title = 'Songs listened per day'),
                yaxis = dict(title = 'Number of days in month listened'),
                )

    # append all charts to the figures list
    graphs = []
    graphs.append(dict(data=graph_one, layout=layout_one))
    graphs.append(dict(data=graph_two, layout=layout_two))

    return graphs
