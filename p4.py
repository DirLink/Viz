import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc

# df = pd.read_excel('C:/Users/uza15050/Documents/Python snippets/demo/mpp_comparison.xlsx')
df = pd.read_excel('C:/Users/uza15050/Documents/Python snippets/demo/mpp_comparison.xlsx', index_col=0)
df['Values'] = df['Values'].round().astype(int)
# df = df[df['Integrated']=='All']
# df_all = pd.read_csv('C:/Users/uza15050/Documents/Python snippets/demo/PBI_ALL.csv')
# df_v33 = pd.read_excel('C:/Users/uza15050/Documents/Python snippets/demo/PBI31.xlsx')
# df_v34 = pd.read_excel('C:/Users/uza15050/Documents/Python snippets/demo/PBI32.xlsx')
lct_options = ['All Locations', 'Almaty', 'Atyrau', 'Farnborough', 'New Delhi', 'Offshore Other', 'Tengiz', ]
type_options = ['FTE', 'HeadCount', 'Hours']
locations = {
        'Almaty': 'rgb(166,206,227)',
        'Atyrau': 'rgb(31,120,180)',
        'Farnborough': 'rgb(227,26,28)',
        'New Delhi': 'rgb(100,388,29)',
        'Offshore Other': 'rgb(251,154,153)',
        'Tengiz': 'rgb(51,160,44)'
        }
# locations = {
#         'Almaty': 'green',
#         'Atyrau': 'orange',
#         'Farnborough': 'cyan',
#         'New Delhi': 'blue',
#         'Offshore Other': 'yellow',
#         'Tengiz': 'red'
#         }

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
fig = go.Figure()

app.layout = html.Div([
    html.H2("MPP Comparison", style={'width': '20%', 'display': 'inline-block', 'vertical-align': '-10%', 'padding-left':'45px', 'padding-right':'0px', 'margin-right':'0px'}),
    html.Div(
        [
            dcc.Dropdown(
                id="location",
                options=[{
                    'label': l,
                    'value': l
                } for l in lct_options],
                value='All Locations',
                clearable=False),
        ],
        style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'middle', 'padding-left':'0px', 'margin-left':'0px'}
    ),
    html.Div(
        [
            dcc.RadioItems(id='integrated', options=['All', 'Integrated','Non-Integrated'], value='All', inline=True, labelStyle={'padding-left':'5px', 'margin-left': '35px'})
        ],
        style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'middle', 'padding-left':'5px'}
    ),

    html.Div(
        [
            dcc.Dropdown(
                id="type",
                options=[{
                    'label': t,
                    'value': t
                } for t in type_options],
                value='FTE',
                clearable=False),
        ],
        style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'middle', 'padding-left':'0px', 'margin-left':'0px'}
    ),

    html.Div(
        [
            dcc.Graph(figure=fig, id='mpp-graph'),
            dcc.RangeSlider(
                id = 'period_slider',
                min=0,
                max=18,
                step=None,
                marks={0: 'Jan-24', 1: 'Feb-24', 2: 'Mar-24', 3: 'Apr-24', 4: 'May-24', 5: 'Jun-24', 6: 'Jul-24', 7: 'Aug-24', 8: 'Sep-24', 9: 'Oct-24',
                       10: 'Nov-24', 11: 'Dec-24', 12: 'Jan-25', 13: 'Feb-25', 14: 'Mar-25', 15: 'Apr-25', 16: 'May-25', 17: 'Jun-25'
                },
                value=[0, 17],
                allowCross=False
            )
        ],
        style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'middle', 'padding-left':'0px', 'margin-left':'0px', 'margin-right':'15px'}
    ),

], style={'width': '100%'})

@app.callback(
    dash.dependencies.Output('mpp-graph', 'figure'),
    dash.dependencies.Input('location', 'value'),
    dash.dependencies.Input('integrated', 'value'),
    dash.dependencies.Input('type', 'value'),
    dash.dependencies.Input('period_slider', 'value'))
def update_graph(location, integrated, type, period_slider):
    print(integrated)
    # Clear existing traces
    fig.data = []
    period = ['01-01-24', '02-01-24', '03-01-24', '04-01-24', '05-01-24', '06-01-24', '07-01-24', '08-01-24', '09-01-24', '10-01-24', '11-01-24', '12-01-24', '01-01-25', '02-01-25', '03-01-25', '04-01-25', '05-01-25', '06-01-25']

    df_v33 = df[(df['Type']==type)&(df['Revision']=='V33')&(df['Integrated']==integrated)].loc[period[period_slider[0]]:period[period_slider[1]]]
    df_v34 = df[(df['Type']==type)&(df['Revision']=='V34')&(df['Integrated']==integrated)].loc[period[period_slider[0]]:period[period_slider[1]]]

    # df_v34 = df[df['Revision']=='V34']

    if location == 'All Locations':
        # Locations = ['Almaty', 'Atyrau', 'Farnborough', 'Offshore Other', 'Tengiz']
        colors = ["rgb(166,206,227)", "rgb(31,120,180)", "rgb(227,26,28)", "rgb(251,154,153)", "rgb(51,160,44)"]
        positions = ['top right', 'top left', 'top right', 'top left', 'top right']

        # for l, c, p in zip(Locations, colors, positions):
        for l, c in locations.items():
            ## put var1 and var2 together on the first subgrouped bar
            fig.add_trace(
                go.Scatter(
                    x=df_v33[df_v33['Location']==l]['Period1'], 
                    y=df_v33[df_v33['Location']==l]['Values'], 
                    name='v33 '+l, 
                    stackgroup='one', 
                    fill='none', 
                    text=df_v33[df_v33['Location']==l]['Values'],
                    line=dict(
                        color=c
                    ),
                    texttemplate="%{y:.0f}",
                    textposition='bottom right',
                    opacity=1,
                    mode='text+lines'),
            )

        # for l, c, p in zip(Locations, colors, positions):
        for l, c in locations.items():
            fig.add_trace(
                go.Bar(
                    x=df_v34[df_v34['Location']==l]['Period1'], 
                    y=df_v34[df_v34['Location']==l]['Values'],  
                    name='v34 '+l, 
                    text=df_v34[df_v34['Location']==l]['Values'],
                    # text_auto='.2s',
                    # text_auto=True,
                    texttemplate="%{y:.0f}",
                    textposition='outside',
                    opacity=1,
                    marker_color=c,
                    width=0.7
                    ),
            )
    else:
        # Add scatter plot trace for v33
        fig.add_trace(
            go.Scatter(
                x=df_v33[df_v33['Location']==location]['Period1'], 
                y=df_v33[df_v33['Location']==location]['Values'], 
                name='v33 '+location,
                # stackgroup='one', 
                fill='none', 
                text=df_v33[df_v33['Location']==location]['Values'],
                line=dict(
                        color=locations[location]
                    ),
                # text=df_v33[Location].fillna(''),  # Replace NaN with ''
                textposition='bottom right',
                opacity=1,
                mode='text+lines'),
        )

        # Add bar plot trace for v34
        fig.add_trace(
            go.Bar(
                x=df_v34[df_v34['Location']==location]['Period1'], 
                y=df_v34[df_v34['Location']==location]['Values'],  
                name='v34 '+location, 
                text=df_v34[df_v34['Location']==location]['Values'],
                # text=df_v34[Location].fillna(''),  # Replace NaN with ''
                textposition='outside',
                opacity=1,
                marker_color=locations[location],
                width=0.7
            ),
        )
    fig.update_layout(
        barmode='stack', 
        uniformtext_minsize=10,
        uniformtext_mode='hide',
        autosize=False,
        width=1800,
        height=700,
        margin=dict(
            l=20,
            r=20,
            b=10,
            t=20,
            pad=0
        ),
        font=dict(
            family="Arial",
            size=10,  # Set the font size here
            color="RebeccaPurple"
        ),
        legend=dict(
            x=0.912,
            y=1,
            traceorder="reversed",
            title_font_family="Times New Roman",
            font=dict(
                family="Arial",
                size=10,
                color="black"
            ),
            bgcolor="LightSteelBlue",
            bordercolor="Black",
            borderwidth=2
        )
    )

    # fig.update_xaxes(showspikes=True)
    # fig.update_yaxes(showspikes=True)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(host='0.0.0.0',debug=True)


