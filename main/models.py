from django.db import models # type: ignore
import yfinance as yf # type: ignore
import plotly.graph_objs as go # type: ignore
from plotly.io import to_json # type: ignore
from plotly.offline import plot # type: ignore
import json
import requests


# Create your models here.
class GetIcon():
    def get_stock_logo(symbol):
        try:
            # Fetch stock information
            ticker = yf.Ticker(symbol)
            
            # Get the info dictionary
            info = ticker.info
            
            # Extract the logo URL
            logo_url = info.get('logo_url', 'Logo URL not found')
            
            return logo_url
        except Exception as e:
            return f"An error occurred: {e}"

class RawData():
    # This Function is created to fetch data of the selected stock/ticker
    def load_data(ticker, startDate, endDate):
        data = yf.download(ticker, startDate, endDate)
        data.reset_index(inplace=True)
        return data


class ChartGraphs():

    def plot_raw_data(data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Opening Price"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Closing Price"))
        fig.layout.update( 
            xaxis_title='-- Time --', 
            yaxis_title='-- Stock Price --', 
            xaxis_rangeslider_visible=True
            )
        
        # Convert Plotly chart to JSON format
        plot_json = to_json(fig)
        return plot_json
    

class ApexCharts():

    def plot_raw_data_apex(data):
        # Prepare data for ApexCharts
        open_data = [{'x': str(date), 'y': open_price} for date, open_price in zip(data['Date'], data['Open'])]
        close_data = [{'x': str(date), 'y': close_price} for date, close_price in zip(data['Date'], data['Close'])]

        # Define ApexCharts options
        apex_options = {
            'chart': {
                'parentHeightOffset': 0,
                'type': 'area',
                # 'toolbar': {'show': False},
                # 'stacked': True,
                'toolbar': {
                    'show': False
                },
            },
            'colors': ['#14de14', '#506fd9'],
            'grid': {
                'borderColor': 'rgba(72,94,144, 0.08)',
                'padding': {'top': 30},
                'yaxis': {
                    'lines': {'show': False},
                },
            },
            'stroke': {
                'curve': 'smooth',
                'width': [2, 1],
            },
            'xaxis': {
                'type': 'datetime',
                # 'tickAmount': 13,
                'axisBorder': {'show': False},
                'labels': {
                    'style': {
                        'colors': '#6e7985',
                        'fontSize': '11px',
                    },
                },
            },
            'yaxis': {
                'show': False,
            },
            'fill': {
                'type': 'gradient',
                'gradient': {
                    'opacityFrom': 0.5,
                    'opacityTo': 0,
                },
            },
            'dataLabels': {'enabled': False},
            # 'legend': {'show': False},
            # 'tooltip': {'enabled': False},
            'series': [
                {
                    'name': 'Opening Price',
                    'data': open_data
                },
                {
                    'name': 'Closing Price',
                    'data': close_data
                }
            ]
        }

        # Convert the options to JSON format
        # plot_json = json.dumps(apex_options)
        return apex_options