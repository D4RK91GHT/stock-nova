from django.db import models
import yfinance as yf

import plotly.graph_objs as go
from plotly.offline import plot

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
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        
        # Save the Plotly chart as an HTML file
        plot_html = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_html