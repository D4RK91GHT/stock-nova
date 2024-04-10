import json
from django.shortcuts import render,redirect
from django.http import JsonResponse
import base64
from datetime import date
from io import BytesIO
from prophet import Prophet
from prophet.plot import plot_plotly
import matplotlib.pyplot as plt
from main.models import RawData,ChartGraphs

APPTITLE    = "Stock Nova"
START       = "2015-01-01"
TODAY       = date.today().strftime("%Y-%m-%d")




rawdata = ['SBIN.NS', 'TCS.NS', 'BHEL.NS', 'IOC.NS', 'RVNL.NS', 'IRFC.NS']

# Convert list to JSON
allTickers = json.dumps(rawdata)


# =======================================
def predections(selected_stock):
    period = 1 * 365
    data = RawData.load_data(selected_stock, START, TODAY)
    oldData = data.tail()
    timeSeries = ChartGraphs.plot_raw_data(data)
    # timeSeries = json.loads(timeSeries)
    # print(timeSeries)

    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    predictedData = forecast.tail()

    fig1 = plot_plotly(m, forecast)
    predictedGraph = fig1.to_json()

    # plt.switch_backend('Agg')

    # fig2 = m.plot_components(forecast)
    # buf = BytesIO()
    # fig2.savefig(buf, format='png', bbox_inches='tight')
    # buf.seek(0)
    # fig2_base64 = base64.b64encode(buf.read()).decode('utf-8')
    # plt.close(fig2)

    plt.switch_backend('Agg')

    fig2 = m.plot_components(forecast)
    buf = BytesIO()
    fig2.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)

    # Convert the PNG image to a base64-encoded string
    fig2_base64 = base64.b64encode(buf.read()).decode('utf-8')


    # Prepare the data to be returned as JSON
    context = {
        # 'data' : selected_stock
        'data': oldData.to_dict(),
        'timeSeries': timeSeries,
        'predictedData': predictedData.to_dict(),
        'predictedGraph': predictedGraph,
        'predictedComponents': fig2_base64
        }
    return context