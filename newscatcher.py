from newscatcherapi import NewsCatcherApiClient
from newsDataStorage import saveNewscatcherData
from newsArticle import Article_text
from sentimentAnalysis import analyzeSentiment
from checkSimilaritiesOfNews import checkSimilarNewsCatcher
from datetime import datetime

newscatcherapi = NewsCatcherApiClient(x_api_key='s3dSya8t7FOjKcowSzrt51myyA9KOOzRIGFT9-PHWR0')

all_articles = newscatcherapi.get_search(q='rwanda',
                                         lang='en',
                                         search_in="title",
                                         sort_by="date"
                                         )
for i in range(len(all_articles['articles'])):
    try:
        source=all_articles['articles'][i]['clean_url']
        title=all_articles['articles'][i]['title']
        publishedAt=all_articles['articles'][i]['published_date']
        summary=all_articles['articles'][i]['summary']
        url=all_articles['articles'][i]['link']
        date_format = "%Y-%m-%d"
        date = datetime.strptime(publishedAt[0:10], date_format)
        article_text=Article_text(url)
        sentiment=analyzeSentiment(article_text)
    except Exception as e:
        continue

    # Save the data only if no error occurred
    check=checkSimilarNewsCatcher(title)
    if(check==True):
        result = saveNewscatcherData(source, title, summary, date, url, sentiment)
        if result == 0:
            print("Unable to save.")
        else:
            print("Saved successfully.")
            print(i)



