from newspaper import Article

def Article_text(url):
    article=Article(url)
    article.download();
    article.parse()
    return article.text



