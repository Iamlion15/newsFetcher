from nltk.sentiment import SentimentIntensityAnalyzer




def analyzeSentiment(text):
    
    # Initialize the VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Perform sentiment analysis
    sentiment_scores = analyzer.polarity_scores(text)

    # Determine the sentiment category based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment_category = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment_category = 'Negative'
    else:
        sentiment_category = 'Neutral'

    return sentiment_category

