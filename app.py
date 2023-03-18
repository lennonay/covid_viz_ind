import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

covid_data = pd.read_csv('data/covid_data.csv')
covid_data['date'] = pd.to_datetime(covid_data['date'])
covid_data = covid_data[(covid_data['continent']).notnull()]

location = list(covid_data.location.unique())
location.append('World')

    
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
        dcc.Graph(id = 'pie_chart'),
        dcc.Graph(id = 'world_map')
        ]),
    dbc.Col([
        dcc.Graph(id = 'total_cases'),
        dcc.Graph(id = 'new_vac')
    ],md=4)
    ])])

# Set up callbacks/backend
@app.callback(
    Output('pie_chart', 'figure'),
    Output('world_map', 'figure'),
    Output('total_cases', 'figure'),
    Output('new_vac', 'figure'),
    Input('xcol', 'value'),
    Input('xslider', 'value'),
    Input('hslider','value')
)
def generate_chart(xcol,xslider,hslider):
    if (xcol != 'World'):
        int_plot = covid_data[covid_data['location'] == xcol]
    else: int_plot = covid_data
    
    age_covid_data = int_plot[(int_plot['median_age'] > xslider[0] ) & (int_plot['median_age'] < xslider[1])]
    df = age_covid_data[(age_covid_data['human_development_index'] > hslider[0] ) & (age_covid_data['human_development_index'] < hslider[1])]
    
    pie_chart = px.pie(df, values='total_cases', names='continent', title='Total Cases of Different Continent')
    
    map_df = pd.DataFrame(df.groupby('location')['stringency_index'].mean().reset_index())
    world_map = px.choropleth(map_df, locations = 'location',locationmode= 'country names',
              color = 'stringency_index', title = 'Mean stringency index of country')
    
    new_vac_df = pd.DataFrame(df.groupby('date')['new_vaccinations_smoothed'].sum().reset_index())
    new_vac = px.line(new_vac_df, x="date", y="new_vaccinations_smoothed",labels = {'new_vaccinations_smoothed': 'New vaccinations smoothed', 'date': 'Date'},title = 'New vaccinations smoothed over time')
    
    total_cases_df = pd.DataFrame(df.groupby('date')['new_cases'].sum().reset_index())
    total_cases_df = total_cases_df.set_index('date')
    total_cases_df = total_cases_df.resample("M").sum()
    total_cases = px.bar(total_cases_df, x=total_cases_df.index, y="new_cases",labels = {'new_cases': 'New Cases', 'date': 'Date'},title = 'News cases by month')


    return pie_chart,world_map,total_cases, new_vac

if __name__ == '__main__':
    app.run_server(debug=True)