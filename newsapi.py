import requests
from newsDataStorage import saveNewsapiData
from newsArticle import Article_text
from articleSummarizer import summarize
from sentimentAnalysis import analyzeSentiment
from checkSimilaritiesOfNews import checkSimilarNewsapi
from datetime import datetime

articles = requests.get("https://newsapi.org/v2/everything?q=rwanda&apiKey=8e193b6af3df46be883f9a3f35dbf152&sortBy=publishedAt&searchIn=title&language=en")
data = articles.json()

for i in range(len(data['articles'])):
    try:
        source=data['articles'][i]['source']['name']
        title=data['articles'][i]['title']
        publishedAt=data['articles'][i]['publishedAt']
        description=data['articles'][i]['description']
        url=data['articles'][i]['url']
        date_format = "%Y-%m-%d"
        date = datetime.strptime(publishedAt[0:10], date_format)
        article_text=Article_text(url)
        summary=summarize(article_text)
        sentiment=analyzeSentiment(article_text)
    except Exception as e:
        continue

    # Save the data only if no error occurred
    check=checkSimilarNewsapi(title)
    if(check==True):
        result = saveNewsapiData(source, title, description, summary, date, url, sentiment)
        if result == 0:
            print("Unable to save.")
        else:
            print("Saved successfully.")
            print(i)




    
