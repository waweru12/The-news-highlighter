from ..requests import get_sources,get_by_category,search_article,get_top_headlines
from flask import render_template, request, redirect, url_for
from . import main

@main.route('/')
def index():
    '''
    View root page function that returns the inndex page and its data
    '''
    title = 'NotableEventsWeatherAndSports'
    source = get_sources()
    top_headlines = get_top_headlines()
    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    elements=[get_by_category(item) for item in categories]

    searched_article = request.args.get('article_query')
    if searched_article:
        name_list=searched_article.split(' ')
        item = '+'.join(name_list)
        return redirect(url_for('main.search', name = item))
    else:
        return render_template( 'source.html', title = title, sources = source, categories = elements,headlines = top_headlines )


    
    

    

@main.route( '/search/<name>' )
def search(name):
    '''
    '''
    searched_articles = search_article(name)
    title = f'search results for {name}'
    return render_template('search.html',articles = searched_articles  )

    