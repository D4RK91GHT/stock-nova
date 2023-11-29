from django.shortcuts import render,redirect
import base64
from datetime import date
from io import BytesIO
from prophet import Prophet
from prophet.plot import plot_plotly
import matplotlib.pyplot as plt
from main.models import RawData,ChartGraphs


# ===================================================

APPTITLE    = "Stock Nova"
START       = "2015-01-01"
TODAY       = date.today().strftime("%Y-%m-%d")


avilableStocs = ['SBI.NS', 'TCS.NS', 'BHEL.NS', 'IOC.NS', 'RVNL.NS', 'IRFC.NS']


context = {
    'name':'Dipak',
    'stock_list': avilableStocs
}


# Create your views here.
def index(request):
    return render(request, 'index.html', context)
# ==================================================


def showdata(request):
    data = {}
    try:
        if request.method == "POST":
          selected_stock  = request.POST.get('stock')

        # slecting the prediction year (Like I want to predict for 1 Year so, period should be in number of days)
        period = 1 * 365

        # Fetching the previous data f the selected stock/ticker
        data = RawData.load_data(selected_stock, START, TODAY)

        # Geeting the data of last few days
        oldData = data.tail()

        # Visualiging the previous data grph of the selected stock/ticker
        timeSeries = ChartGraphs.plot_raw_data(data)


        # ===================================================

        # Predict forecast with Prophet.
        df_train = data[['Date', 'Close']]
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

        m = Prophet()
        m.fit(df_train)
        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)

        # Show and plot forecast
        predictedData = forecast.tail()
        # print(predictedData)

        # st.write(f'Forecast plot for {n_years} years')
        fig1 = plot_plotly(m, forecast)
        predictedGraph = fig1.to_json()

        # Set the Matplotlib backend to 'Agg' to avoid the warning
        plt.switch_backend('Agg')

        # st.write("Forecast components")
        fig2 = m.plot_components(forecast)
        # predictedComponents = fig2.to_json()


        buf = BytesIO()
        fig2.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        fig2_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig2)


        context = {
            'data' : oldData,
            'timeSeries' : timeSeries,
            'predictedData' : predictedData,
            'predictedGraph' : predictedGraph,
            'predictedComponents' : fig2_base64
        }
        return render(request, 'showdata.html', context)
    except:
        pass
# ===================================================