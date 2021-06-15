from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField('Name', max_length=240)
    email = models.EmailField()
    wishlist = models.ForeignKey(product, on_delete=models.CASCADE)
    registationDate = models.DateField('Registration Date', auto_now_add = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Name', maxLength=240)
    #FOR WHEN WE HAVE IMAGE UPLOADS>> picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)