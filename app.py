import pandas as pd
from statsbombpy import sb
from mplsoccer import Pitch
import seaborn as sns
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import seaborn as sns
import os
from urllib.request import urlopen
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from mplsoccer import PyPizza, add_image, FontManager

import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
from matplotlib.colors import LinearSegmentedColormap
from mplsoccer import Pitch, FontManager
from mplsoccer import Pitch, VerticalPitch, FontManager, Sbopen
import numpy as np

import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from PIL import Image
import wikipediaapi

# set configurations

# Font configuration
font_normal = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto%5Bwdth,wght%5D.ttf')
font_italic = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto-Italic%5Bwdth,wght%5D.ttf')
font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                        'RobotoSlab%5Bwght%5D.ttf')

# colormap configuration
pearl_earring_cmap = LinearSegmentedColormap.from_list("Pearl Earring - 10 colors",
                                                       ['#15242e', '#4393c4'], N=10)

# Get data from StatsBomb
competitions = sb.competitions()
matches = sb.matches(competition_id=55, season_id=43)
events = sb.events(match_id=3794686)
match = pd.read_json(f'./open-data/data/three-sixty/{3794686}.json')
df = pd.merge(left=events, right=match, left_on='id', right_on='event_uuid', how='left')

# Remove rows with null values in column 'player' and 'location'
df = df.dropna(subset=['player', 'location'])

# Create a dictionary of descriptions per player
players = ['Pedro González López', 'Aymeric Laporte', 'Joško Gvardiol', 'Bruno Petković', 'Eric García Martret',
           'Marcelo Brozović', 'Sergio Busquets i Burgos', 'César Azpilicueta Tanco', 'José Luis Gayà Peña',
           'Pablo Sarabia García', 'Jorge Resurrección Merodio', 'Ante Rebić', 'Dominik Livaković',
           'Unai Simón Mendibil', 'Ferrán Torres García', 'Álvaro Borja Morata Martín', 'Mateo Kovačić',
           'Josip Juranović', 'Domagoj Vida', 'Luka Modrić', 'Duje Ćaleta-Car', 'Nikola Vlašić',
           'Andrej Kramarić', 'Pau Francisco Torres', 'Mislav Oršić', 'Daniel Olmo Carvajal', 'Josip Brekalo',
           'Fabián Ruiz Peña', 'Jordi Alba Ramos', 'Ante Budimir', 'Mario Pašalić', 'Mikel Oyarzabal Ugarte',
           'Rodrigo Hernández Cascante', 'Luka Ivanušec']

wiki_wiki = wikipediaapi.Wikipedia('en')

player_descriptions = {}

for player in players:
    page = wiki_wiki.page(player)
    if page.exists():
        player_descriptions[player] = page.summary
    else:
        player_descriptions[player] = "La página de Wikipedia para '%s' no existe." % player

# CSS styling settings
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    className='container',
    children=[
        html.H1('Passes Visualization', className='mt-4 mb-4'),
        dcc.Dropdown(
            id='player-dropdown',
            options=[{'label': player, 'value': player} for player in df['player'].unique()],
            value=df['player'].unique()[0],
            className='form-control'
        ),
        html.Div(id='player-description', className='mt-4 mb-4'),  # Div to display the player's description
        dcc.Graph(id='passes-graph')
    ]
)

@app.callback(
    Output('passes-graph', 'figure'),
    [Input('player-dropdown', 'value')]
)
def update_graph(selected_player):
    # Filter the rows of the DataFrame by the selected player
    filtered_df = df[df['player'] == selected_player].copy()

    # Create the scatterplot with Plotly
    fig = go.Figure(data=go.Scatter(
        x=filtered_df['location'].apply(lambda loc: loc[0]),
        y=filtered_df['location'].apply(lambda loc: loc[1]),
        mode='markers',
        marker=dict(size=10, color='red')
    ))

    # configure the chart layout
    fig.update_layout(
        title=f"Passes Visualization - {selected_player}",
        xaxis=dict(
            title=None,  
            showgrid=False, 
            showticklabels=False,
            zeroline=False
        ),
        yaxis=dict(
            title=None,  
            showgrid=False,  
            showticklabels=False, 
            zeroline=False  
        ),
        autosize=False,
        width=698,
        height=480,
        showlegend=False
    )


    # Load the image of the soccer field
    field_image = Image.open('./plotly_add_pitch.png')

    # Add the background image to the graphic
    fig.add_layout_image(
        source=field_image,
        x=0,
        y=80,
        xref='x',
        yref='y',
        sizex=120,
        sizey=80,
        sizing='stretch',
        opacity=0.9,
        layer='below'
    )

    return fig

@app.callback(
    Output('player-description', 'children'),
    [Input('player-dropdown', 'value')]
)
def update_player_description(selected_player):
    # Get the description of the selected player
    description = player_descriptions.get(selected_player, '')

    return html.P(description, className='text-justify')

if __name__ == '__main__':
    app.run_server(debug=False, port=8050)