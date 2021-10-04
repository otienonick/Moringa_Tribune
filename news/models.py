from django.db import models
import datetime as dt



# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)


    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save() 
        
          
    class meta:
        ordering =['first_name']
  

class tags(models.Model):
    name = models.CharField(max_length = 30)    

    def __str__(self):
        return self.name
 

class Article(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete = models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
  
#  DateTimeField to store the exact date and time our article was posted
#  We pass in the argument auto_now_add and equate it to True. This will automatically save the exact time and date to the database as soon as we save that model.

   