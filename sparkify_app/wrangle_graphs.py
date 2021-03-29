import pandas as pd
import plotly.graph_objs as go
#import plotly.express as px
import joblib

def return_graphs(df):
    """Creates four plotly visualizations
    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """

    # extract data for visuals
    #sb.countplot(x='gender', data=df);

    #categories = df.iloc[:,4:40].sum().sort_values(ascending=False)
    #categories_names = categories.index.to_series().apply(lambda x: x.replace('_', ' '))
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
    # graph_two = []
    # graph_two.append(
    #   go.Bar(
    #   x = genre_names,
    #   y = genre_counts,
    #   )
    # )
    # layout_two = dict(title = 'Distribution of Message Genres',
    #             xaxis = dict(title = 'Genre'),
    #             yaxis = dict(title = 'Count'),
    #             )
    #
    # graph_three = []
    # # https://stackoverflow.com/questions/57639371/plotly-scatter-isnt-displayed-by-flask
    # graph_three = go.Figure()
    # graph_three.add_trace(go.Scatter(
    #     x = scatter.index[scatter.type=='including stopwords'],
    #     y = scatter.message[scatter.type=='including stopwords'],
    #     name = 'including stopwords',
    #     mode = 'markers'
    # ))
    # graph_three.add_trace(go.Scatter(
    #     x = scatter.index[scatter.type=='without stopwords'],
    #     y = scatter.message[scatter.type=='without stopwords'],
    #     name = 'without stopwords',
    #     mode = 'markers'
    # ))
    # graph_three.update_layout(title='Word count per message',
    #     xaxis_title='Words per Message', yaxis_title='Count')
    # layout_three = ()

    # append all charts to the figures list
    graphs = []
    graphs.append(dict(data=graph_one, layout=layout_one))
    graphs.append(dict(data=graph_two, layout=layout_two))
    #graphs.append(dict(data=graph_three, layout=layout_three))

    return graphs
