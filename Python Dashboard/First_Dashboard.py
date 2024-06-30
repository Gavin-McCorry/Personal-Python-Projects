from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import numpy


app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Creating the layout for the dashboard, this makes an empty DIV containter
# app.layout = html.Div()

# Make the dashboard take up 100% width of any browsre window by making it fluid
#app.layout = dbc.Container(fluid=True)

# For the container to appear on the screen it must contain somehting, so weput some temprary text in it for now
#app.layout = dbc.Container(html.P("My awesome dashboard will be here"),
#                           fluid=True)

# Styling the body of our dashboard
#app.layout = dbc.Container(html.P("My awesome dashboard will be here."),
#                           fluid=True,
#                           className='dashboard-container')

# When styling our app we need to keep in mind the hierarchy of the css files
# The order our app follows instructiosn is it first looks for the elements style in our custom file,
# and then it will look for th elements style in our Bootstrap file.
# IE: it will look at the elements stylinng in our Style.css fil first, and then will use a defualt style that we set,
# example above is the ecternalstylesheets = ...

# We can also style any individual element direclty from the app, and this style ranks higher then both
# custom CSS and Bootstrap CSS.
# EX: wee can change th ecolor of the dashboard t white, its boarder to black, and the text color to black:

# app.layout = dbc.Container(html.P("My awesome dashboard will be here.",
#                                   style={'color': '#010103'}),
#                            fluid=True,
#                            className='dashboard-container',
#                            style={
#                                'background-color': '#ffffff',
#                                'border-color': '#010103'
#                            })

# Now w have the body of our dashboard, we can start layering our DIV containers on top of it
# The first lasyer is going to divide the dashboard into two parts
# When doing this w also specify the dimensions for each section of the dashboard,
# we can do this by specifying the dimensions in pxels or in percentages

# app.layout = dbc.Container([
#     html.Div(style={
#         'width': 340,
#         'margin-left': 35,
#         'margin-top': 35,
#         'margin-bottom': 35
#     }),
#     html.Div(
#         style={
#             'width': 990,
#             'margin-top': 35,
#             'margin-right': 35,
#             'margin-bottom': 35
#         })
# ],
#     fluid=True,
#     style={'display': 'flex'},
#     className='dashboard-container')

# Now we mov on to the second layre, our left "navigation" containeer is divided into 4 parts,
# the title and descriptio, the button bar, an dropdown meno, and an image.
# knowing this lets put a lit of 4 empty DIV containeers in it.
# th right part consits of a graph and its output, so well put a list of 2 DIVS in it

# app.layout = dbc.Container([
#     html.Div([html.Div(), html.Div(),
#               html.Div(), html.Div()],
#              style={
#                  'width': 340,
#                  'margin-left': 35,
#                  'margin-top': 35,
#                  'margin-bottom': 35
#              }),
#     html.Div(
#         [html.Div(style={'width': 790}),
#          html.Div(style={'width': 200})],
#         style={
#             'width': 990,
#             'margin-top': 35,
#             'margin-right': 35,
#             'margin-bottom': 35,
#             'display': 'flex'
#         })
# ],
#     fluid=True,
#     style={'display': 'flex'},
#     className='dashboard-container')

# Now we can start filling our dahboard with content. For the top left navigation panel, we
# havee the title of the dashboard and the introduction text.
# Since our dashboard only has a head and onetype of tet, we can get by
# using common tags and not introductiong classes or IDS

app.layout = dbc.Container([
    html.Div(
    [html.Div([
                html.H1([
                    html.Span("Welcome"),
                    html.Br(),
                    html.Span("to my beautiful dashboard!")
                ]),
                html.P("This dashboard prototype shows how to create an effective layout.")
            ],
                style={
                    "vertical-alignment": "top",
                    "height": 260
                }),
            html.Div(),
            html.Div(),
            html.Div()],
             style={
                 'width': 340,
                 'margin-left': 35,
                 'margin-top': 35,
                 'margin-bottom': 35
             }),
    html.Div(
        [html.Div(style={'width': 790}),
         html.Div(style={'width': 200})],
        style={
            'width': 990,
            'margin-top': 35,
            'margin-right': 35,
            'margin-bottom': 35,
            'display': 'flex'
        })
],
    fluid=True,
    style={'display': 'flex'},
    className='dashboard-container')


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)


