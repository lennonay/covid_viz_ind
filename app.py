import dash
from dash import html, dcc, Input, Output
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd

alt.data_transformers.enable('data_server')


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

covid_data = pd.read_csv('data/covid_data.csv')
covid_data['date'] = pd.to_datetime(covid_data['date'])
covid_data = covid_data[(covid_data['continent']).notnull()]

location = list(covid_data.location.unique())
location.append('World')

def plot_cases(country, median_age, human_index):
    if (country != 'World'):
        toal_case_plot = covid_data[covid_data['location'] == country]
    else: toal_case_plot = covid_data
    age_covid_data = toal_case_plot[(toal_case_plot['median_age'] > median_age[0] ) & (toal_case_plot['median_age'] < median_age[1])]
    df = age_covid_data[(age_covid_data['human_development_index'] > human_index[0] ) & (age_covid_data['human_development_index'] < human_index[1])]
    df = pd.DataFrame(df.groupby('date')['total_cases'].sum().reset_index())
    chart = alt.Chart(df, title = 'Total cases over time').mark_line().encode(
        x='date',
        y='total_cases',
        tooltip = alt.Tooltip('total_cases',format = ',')
    ).properties(
    width=800,
    height=280).interactive()
    return chart.to_html()

def plot_vaccinations(country, median_age, human_index):
    if (country != 'World'):
        toal_case_plot = covid_data[covid_data['location'] == country]
    else: toal_case_plot = covid_data
    age_covid_data = toal_case_plot[(toal_case_plot['median_age'] > median_age[0] ) & (toal_case_plot['median_age'] < median_age[1])]
    df = age_covid_data[(age_covid_data['human_development_index'] > human_index[0] ) & (age_covid_data['human_development_index'] < human_index[1])]
    df = pd.DataFrame(df.groupby('date')['new_vaccinations_smoothed'].sum().reset_index())
    chart = alt.Chart(df, title = 'New vaccinations smoothed over time').mark_line().encode(
        x='date',
        y='new_vaccinations_smoothed',
        tooltip = alt.Tooltip('new_vaccinations_smoothed',format = ',')
    ).properties(
    width=800,
    height=280).interactive()
    return chart.to_html()


app.layout = dbc.Container([
    html.H1('COVID Dashboard',style={
                    'backgroundColor': 'steelblue',
                    'padding': 20,
                    'color': 'white',
                    'margin-top': 20,
                    'margin-bottom': 20,
                    'text-align': 'center',
                    'font-size': '48px',
                    'border-radius': 3}),
    dbc.Row([dbc.Col(
        [
           'Select World / country',
            dcc.Dropdown(
            id='xcol', value='World',
            options=[{'label': i, 'value': i} for i in location]),
            'Select range for median age',
            dcc.RangeSlider(10,50, value=[10, 50], id='xslider'),
            'Select range for human development index',
            dcc.RangeSlider(0.3,1, value=[0.3, 1], id='hslider')
        ],md=3,style={
                'background-color': '#e6e6e6',
                'padding': 15,
                'border-radius': 3}),
    dbc.Col([
        html.Iframe(
            id = 'total_cases',
            srcDoc=plot_cases('World',[15,35],[0.3,1]),
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        html.Iframe(
            id = 'total_vaccinations',
            srcDoc=plot_vaccinations('World',[15,35],[0.3,1]),
            style={'border-width': '0', 'width': '100%', 'height': '400px'})
    ])])])

# Set up callbacks/backend
@app.callback(
    Output('total_cases', 'srcDoc'),
    Output('total_vaccinations', 'srcDoc'),
    Input('xcol', 'value'),
    Input('xslider', 'value'),
    Input('hslider','value')
)

def update_output(xcol,xslider,hslider):
    return plot_cases(xcol,xslider,hslider), plot_vaccinations(xcol,xslider,hslider)

if __name__ == '__main__':
    app.run_server(debug=True)