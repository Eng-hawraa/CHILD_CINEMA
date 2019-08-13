from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class Cinema(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now='')
    content = models.TextField(null=False)
    pic = models.ImageField('default.jpg', upload_to='profile_pics')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Meta:
    ordering = ('-date',)
    


# python manage.py makemigrations
# python manage.py migrate