import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY="IGA7PQW68PK9U7AM"
NEWS_API_KEY="3603d163743149969facee817a7d79a6"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
response=requests.get(STOCK_ENDPOINT,params=stock_params)
data=response.json()['Time Series (Daily)']
data_list=[value for(key,value) in data.items()]
yesterday_closing_price=data_list[0]['4. close']

before_yesterday_closing_price=data_list[1]['4. close']
delta=abs(float(yesterday_closing_price)-float(before_yesterday_closing_price))
delta_percent=delta/float(yesterday_closing_price)*100
if(delta_percent>5):
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()

    articles = articles[:3]
    print(articles)

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]
    client=Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        client.messages.create(body=article,from_="+1 8669356050",to="+14046696896")







