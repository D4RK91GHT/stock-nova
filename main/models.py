from django.db import models # type: ignore
import yfinance as yf # type: ignore
import plotly.graph_objs as go # type: ignore
from plotly.io import to_json # type: ignore
from plotly.offline import plot # type: ignore


# Create your models here.

class RawData():
    # This Function is created to fetch data of the selected stock/ticker
    def load_data(ticker, startDate, endDate):
        data = yf.download(ticker, startDate, endDate)
        data.reset_index(inplace=True)
        return data


class ChartGraphs():

    def plot_raw_data(data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Stock Open"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Stock Close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    
        # Convert Plotly chart to JSON format
        plot_json = to_json(fig)
        return plot_json