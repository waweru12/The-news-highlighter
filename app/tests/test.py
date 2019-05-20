import unittest
from app.models import Source
from app.models import Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('KTN', 'KTN-NEWS', 'Home of News', 'https://ktn.co.ke', 'general', 'ke')

    def test_instance(self):
        '''
        Test to check if new_source instance exists
        '''
        self.assertTrue(isinstance(self.new_source,Source))

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Wekesa', 'Kenyan Cars', 'The variety and rich culture that exists in Kenyan motorsport', 'https://ktn.co.ke', 'https://ktn.co.ke/image1', '24/06/2012', 'kenyan motorshow is among the best')

    def test_instance(self):
        '''
        Test to check if new_Article instance exists
        '''
        self.assertTrue(isinstance(self.new_article,Article))

