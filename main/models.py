from django.db import models # type: ignore
from django.utils import timezone # type: ignore
import yfinance as yf # type: ignore

import plotly.graph_objs as go # type: ignore
from plotly.io import to_json # type: ignore
from plotly.offline import plot # type: ignore


class RegisterUser(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    registration_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email



# Create your models here.
class StocksList(models.Model):
    avilableStocs = ['SBI.NS', 'TCS.NS', 'BHEL.NS', 'IOC.NS', 'RVNL.NS', 'IRFC.NS']
    

class RawData():
    # This Function is created to fetch data of the selected stock/ticker
    def load_data(ticker, startDate, endDate):
        data = yf.download(ticker, startDate, endDate)
        data.reset_index(inplace=True)
        return data


class ChartGraphs():
    
    # def plot_raw_data(data):
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Stock Open"))
    # fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Stock Close"))
    # fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    
    # # Convert Plotly chart to JSON format
    # plot_json = to_json(fig)
    # return plot_json

    def plot_raw_data(data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Stock Open"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Stock Close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        
        # Save the Plotly chart as an HTML file
        # plot_html = plot(fig, output_type='div', include_plotlyjs=False)
        # return plot_html
    
        # Convert Plotly chart to JSON format
        plot_json = to_json(fig)
        return plot_json