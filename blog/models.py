from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):   #Post is the name of the model...Class is defining the object
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  #link to another model
    title = models.CharField(max_length=200)  #define field with a limited number of characters
    text = models.TextField()  #long text with no limit  ie ()
    created_date = models.DateTimeField(default=timezone.now)   #date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
