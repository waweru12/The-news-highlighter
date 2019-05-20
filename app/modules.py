class Source:
    '''
    '''
    def __init__(self, id, name, description, language, category, country, url):
        '''
        '''
        self.id = id
        self.name = name
        self.description = description
        self.language = language
        self.category = category
        self.country = country
        self.url = url

class Article:
    '''
    '''
    def __init__(self, author, title, description, url, urlToImage, publishedAT, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAT = publishedAT
        self.content = content