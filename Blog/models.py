from django.db import models
from django.utils.html import format_html 
from django.contrib.auth.models import User #to get the user model

## category model 
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #foreign key linking to the user model
    id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to='profile_images', default='defaultprofile.png')
    location = models.CharField(max_length=100, blank=True) 
    def __str__(self):
        return self.user.username #return the username of the user note as user1 and user2 etc

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%; " />'.format(self.image.url))
    def __str__(self) -> str:
        return self.title
    
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)  ## jab post delete ho to category bhi delete ho jaaye
    image = models.ImageField(upload_to='post/', default='defaultprofile.png')
    author = models.CharField(max_length=100, default='admin')

    def image_tag(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%; " />'.format(self.image.url))
    def __str__(self) -> str:
        return self.title
    
    