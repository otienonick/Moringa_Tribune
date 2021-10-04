from datetime import date, timedelta
from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt


# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nick = Editor(first_name = 'Nick', last_name ='Otieno', email ='nick@moringaschool.com',phone_number = '0778250250')


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nick,Editor))  

    # Testing Save Method
    def test_save_method(self):
        self.nick.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)   

   

class ArticleTestClass(TestCase):

        def setUp(self):
 
            # Creating a new editor 
            self.nick = Editor(first_name = 'Nick', last_name ='Otieno', email ='nick@moringaschool.com',phone_number = '0778250250')
            self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.nick , pub_date = '22-05-2015')

            # Creating a new tag 
            self.new_tag = tags(name = 'testing')

        # Testing  instance

        def test_instance(self):
            self.assertTrue(isinstance(self.new_article,Article))  

        def test_save_article(self):
            self.nick.save_editor()
            self.new_article.save()
            self.new_tag.save()

        def tearDown(self):
            Editor.objects.all().delete()
            tags.objects.all().delete()
            Article.objects.all().delete()

        def test_delete_articles(self):
            Editor.objects.all().delete()
            tags.objects.all().delete()
            Article.objects.all().delete()

      
        



     


   