import os
import urllib.request,json
from .modules import Source, Article

#Getting the api key
api_key = None

# Getting the news base url
category_url = None
search_url = None
sources_url = None
top_headlines_url = None
everything_url = None

def configure_request(app):
    global api_key, sources_url, top_headlines_url, everything_url, category_url,search_url
    api_key = os.environ.get('NEWS_API_KEY')
    category_url = app.config['CATEGORY_URL']
    search_url = app.config['SEARCH_URL']
    sources_url = app.config['SOURCES_URL']
    top_headlines_url = app.config['TOP_HEADLINES_URL']
    everything_url = app.config['EVERYTHING_URL']



def get_by_category(category):
    '''
    Function that gets the json response to our url request
    '''
    get_category_url = category_url.format(category,api_key)

    with urllib.request.urlopen(get_category_url) as url:
        category_data = url.read()
        category_response = json.loads(category_data)

        all_category_sources = []

        if category_response['sources']:
            category_sources_list = category_response['sources']
            all_category_sources = process_sources(category_sources_list)

            return all_category_sources

def search_article(name):
    '''
    '''

    get_search_result_url = search_url.format(name, api_key)

    with urllib.request.urlopen(get_search_result_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_results = []

        if search_article_response['articles']:
            search_list = search_article_response['articles']
            search_results = process_news(search_list)

            return search_results

def get_sources():
    '''
    '''
    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        all_news_sources = []

        if sources_response['sources']:
            news_sources_list = sources_response['sources']
            all_news_sources = process_sources(news_sources_list)

            return all_news_sources

def get_top_headlines():
    '''
    '''
    get_headlines_url = top_headlines_url.format(api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        headlines_data = url.read()
        headlines_response = json.loads(headlines_data)

        all_headlines_list = []

        if headlines_response['articles']:
            headlines_list = headlines_response['articles']
            all_headlines_list = process_news(headlines_list)

            return all_headlines_list



# def view_source(source_id):
#     get_source_news_url = everything_url.format(source_id, api_key)

#     with urllib.request.urlopen(get_source_news_url) as url:
#         source_news_data = url.read()
#         source_news_response = json.loads(source_news_data)

#         source_articles = None

#         if source_news_response['articles']:
#             source_news_list = source_news_response['articles']
#             source_articles = process_news(source_news_list)

#             return source_articles

def process_news(articles_list):
    '''
    Function that processes the news articles and transform them to a list of objects

    Args:
        article_list:A list of dictionaries that contain news details

    Returns:
           news_results:a list of news objects
    '''
    source_results = []
    for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        if urlToImage:
            article_object = Article(author, title, description, url, urlToImage, publishedAt, content)
            source_results.append(article_object)

    return source_results

def process_sources(sources_list):

    '''
    Function  that processes the news sources and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain sources details
    Returns :
        all_news_sources: A list of source objects
    '''
    all_news_sources = []
    for news_source in sources_list:
        id = news_source.get('id')
        name = news_source.get('name')
        description = news_source.get('description')
        url = news_source.get('url')
        category = news_source.get('category')
        language = news_source.get('language')
        country = news_source.get('country')

        source_object = Source(id,name,description,language,category,country,url)
        all_news_sources.append(source_object)
    
    return all_news_sources

    
    
