from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default="Anonymous-User")
    email = models.EmailField(blank=True)
    describe = models.TextField(default="Sorry..! Book description is not available right now. Please wait we'll update soon.")
    
    def __str__(self):
        return self.name