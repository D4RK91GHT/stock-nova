from django.db import models # type: ignore
import yfinance as yf # type: ignore
import plotly.graph_objs as go # type: ignore
from plotly.io import to_json # type: ignore
from plotly.offline import plot # type: ignore
import json


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
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Opening Price"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Closing Price"))
        fig.layout.update(title_text='Time Series data with Rangeslider',  xaxis_title='-- Time --',
        yaxis_title='-- Stock Price --',xaxis_rangeslider_visible=True)
    
        # Convert Plotly chart to JSON format
        plot_json = to_json(fig)
        return plot_json
    

class ApexCharts():

        
    # def plot_raw_data_apex(data):
    #     # Prepare data for ApexCharts
    #     open_data = [{'x': str(date), 'y': open_price} for date, open_price in zip(data['Date'], data['Open'])]
    #     close_data = [{'x': str(date), 'y': close_price} for date, close_price in zip(data['Date'], data['Close'])]

    #     # Define ApexCharts options
    #     apex_options = {
    #         'chart': {
    #             'type': 'line',
    #             'height': 350,
    #             'zoom': {
    #                 'enabled': True
    #             }
    #         },
    #         'dataLabels': {
    #             'enabled': False
    #         },
    #         'stroke': {
    #             'curve': 'smooth'
    #         },
    #         'title': {
    #             'text': 'Time Series data with Rangeslider',
    #             'align': 'left'
    #         },
    #         'xaxis': {
    #             'type': 'datetime',
    #             'title': {
    #                 'text': '-- Time --'
    #             }
    #         },
    #         'yaxis': {
    #             'title': {
    #                 'text': '-- Stock Price --'
    #             }
    #         },
    #         'series': [
    #             {
    #                 'name': 'Stock Open',
    #                 'data': open_data
    #             },
    #             {
    #                 'name': 'Stock Close',
    #                 'data': close_data
    #             }
    #         ]
    #     }

    #     # Convert the options to JSON format
    #     plot_json = json.dumps(apex_options)
    #     return plot_json

    def plot_raw_data_apex(data):
        # Prepare data for ApexCharts
        open_data = [{'x': str(date), 'y': open_price} for date, open_price in zip(data['Date'], data['Open'])]
        close_data = [{'x': str(date), 'y': close_price} for date, close_price in zip(data['Date'], data['Close'])]

        # Define ApexCharts options
        apex_options = {
        #     'chart': {
        #         'type': 'area',
        #         'height': 430,
        #         'zoom': {
        #             'enabled': True
        #         }
        #     },
        #     'dataLabels': {
        #         'enabled': False
        #     },
        #     'stroke': {
        #         'curve': 'smooth'
        #     },
        #     'xaxis': {
        #         'type': 'datetime',
        #     },
        #    'yaxis': {
        #         'show': False,
        #     },
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