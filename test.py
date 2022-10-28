from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
app = Dash(__name__)


app.layout = html.Div([
    html.H4('Interactive scatter plot'),
    dcc.Graph(id="scatter-plot"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0: '0', 2.5: '2.5'},
        value=[0.5, 2]
    ),
])


@app.callback(
    Output("scatter-plot", "figure"), 
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
        df = pd.read_csv("rgx_new1.csv")
        df1 = df[df["motif"]!="others"]
        df2 = df[df["motif"]=="others"]
        

        # fig = px.scatter(
        # df2, y="dPSI", x="dPSI_df2", 
        # color="motif",  
        # hover_data=["GeneSymbol_df2", "motif","dPSI"], trendline="ols" )
        color_discrete_map = {'BAGAgta': 'rgb(255,0,0)', 'ABGAgta': '#50C878', 'AAGAgta': 'rgb(0,0,255)'}
        fig = px.scatter(
        df1, y="dPSI", x="dPSI_df2", 
        color="motif",  
        hover_data=["GeneSymbol_df2"], trendline="ols",color_discrete_map=color_discrete_map)        
        #    data  = [go.Scatter(
        # df2["dPSI"], df2["dPSI_df2"], 
        # color="motif",  
        # hover_data=["GeneSymbol_df2", "motif","dPSI"], trendline="ols" )]
        # )
        # fig.add_trace(go.Scatter(x=df2["dPSI"], y=df2["dPSI_df2"], mode='markers'))
        fig.update_yaxes(range=[-100, 100])
        fig.update_layout(autosize=False,width=800, height=800,)
        fig.update_xaxes(title='RGX-0014248_175 nM')
        fig.update_yaxes(title='RGX-0136451_175 nM')
        # fig.data = (fig.data[1],fig.data[0])
        return fig



app.run_server(debug=True)

