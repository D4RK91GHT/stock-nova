import json
from django.shortcuts import render,redirect
from django.http import JsonResponse
import base64
from datetime import date
from io import BytesIO
from prophet import Prophet
from prophet.plot import plot_plotly
import matplotlib.pyplot as plt
from main.models import RawData, ChartGraphs, ApexCharts, GetIcon
import pandas as pd
import yfinance as yf # type: ignore

APPTITLE    = "Stock Nova"
START       = "2015-01-01"
TODAY       = date.today().strftime("%Y-%m-%d")
# TODAY       = "2023-01-01"

# TODAY       = "2023-01-01"



def nse_list():
    
    # Load the CSV file
    nse_stocks_df = pd.read_csv('static/NSELIST.csv')
    
    # Trim whitespace from headers
    nse_stocks_df.columns = nse_stocks_df.columns.str.strip()
    
    # Convert DataFrame to list of dictionaries, including required columns
    stocks_list = nse_stocks_df[['SYMBOL', 'NAME_OF_COMPANY', 'SERIES', 'DATE_OF_LISTING', 'ISIN_NUMBER']].to_dict(orient='records')
    
    # Return the data as a JSON response
    return stocks_list



def currentMarket(selected_stock):
    data = RawData.load_data(selected_stock, "2023-01-01", TODAY)
    marketData = ApexCharts.plot_raw_data_apex(data)
    stock = yf.Ticker(selected_stock)
    info = stock.info
    
    # the ticker symbol of the stock you're selected
    logo_url = GetIcon.get_stock_logo(selected_stock)

    context = {
        'res': {
            'logo': logo_url,
            'market': marketData,
            'info': info
        }
            
    }
    return context


# =======================================
def predections(selected_stock, days=90):
    period = 1 * int(days)
    data = RawData.load_data(selected_stock, START, TODAY)
    oldData = data
    timeSeries = ChartGraphs.plot_raw_data(data)

    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    predictedData = forecast

    fig1 = plot_plotly(m, forecast)
    fig1.update_layout(
        autosize=True,
        xaxis_title='Time',
        yaxis_title='Stock Price',
    )
    predictedGraph = fig1.to_json()

    plt.switch_backend('Agg')

    fig2 = m.plot_components(forecast)
    buf = BytesIO()
    fig2.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)

    # Convert the PNG image to a base64-encoded string
    fig2_base64 = base64.b64encode(buf.read()).decode('utf-8')


    # the ticker symbol of the stock you're selected
    logo_url = GetIcon.get_stock_logo(selected_stock)

    # Prepare the data to be returned as JSON
    context = {
        # 'data' : selected_stock
        'info': {'logo': logo_url}, 
        'data': oldData.to_dict(),
        'timeSeries': timeSeries,
        'predictedData': predictedData.to_dict(),
        'predictedGraph': predictedGraph,
        'predictedComponents': fig2_base64
        }
    return context


def predictedGraph(selected_stock, days=90):
    period = 1 * int(days)
    data = RawData.load_data(selected_stock, START, TODAY)
   
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    fig1 = plot_plotly(m, forecast)
    fig1.update_layout(
        autosize=True,
        xaxis_title='Time',
        yaxis_title='Stock Price',
    )
    predictedGraph = fig1.to_json()

    # the ticker symbol of the stock you're selected
    logo_url = GetIcon.get_stock_logo(selected_stock)
    print(f"Logo URL for {selected_stock}: {logo_url}")

    # Prepare the data to be returned as JSON
    context = {
        # 'data' : selected_stock
        'info': {'logo': logo_url},
        'graph': predictedGraph,
        }
    return context