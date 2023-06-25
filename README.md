# Passes Visualization


<div align="center">
    <img src="https://thedatascientist.digital/img/logo.png" alt="Logo" width="25%">
</div>


The "Passes Visualization" project is a complex data visualization application that focuses on visualizing passes in a football match. It provides a user-friendly interface for users to select a specific player and visualize the passes made by that player in the match.

## Features

- Utilizes the Plotly library and its Graph component to create interactive scatter plots.
- Each pass made by the selected player is represented as a point on the graph, with the x and y position indicating the coordinates of the pass on the football field.
- Passes are highlighted in red for better visibility in the graph.
- Provides additional information about the players by utilizing the Wikipedia API to display brief player descriptions alongside the graph.
- Offers an intuitive user interface with a dropdown menu for player selection.
- Automatic update of the visualization to display the corresponding passes based on the selected player.
- Styled with CSS to provide an attractive appearance and a pleasant user experience.

## How to Run

1. Clone or download the repository to your local machine.
2. Ensure you have the required dependencies installed (refer to the project's requirements file). 

Run:

```
pip install -r requirements.txt

```

3. Run the app:
3.1 Run the app.py file using Python: python app.py.

3.1.2 Access the application in your web browser at http://localhost:8050 (or the specified port)

3.2 Run Python Jupyter Notebook.

## Dependecies

- pandas
- statsbombpy
- mplsoccer
- seaborn
- matplotlib
- urllib
- Pillow
- PyPizza
- scipy
- plotly
- dash
- dash_core_components
- dash_html_components
- wikipediaapi

## Usage


1. Open the application in your web browser.
2. Select a player from the dropdown menu to visualize their passes in the match.
3. The scatter plot will update dynamically to display the selected player's passes on the football field.
4. Additional player information is displayed alongside the graph to provide context and insights.

## Contribution

Contributions to the "Passes Visualization" project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).