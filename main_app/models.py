from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=240)
    email = models.EmailField()
    wishlist = models.ForeignKey('Sub', on_delete=models.CASCADE)
    registationDate = models.DateField('Registration Date', auto_now_add = True)

    def __str__(self):
        return self.name


class SubPost(models.Model):
    name = models.CharField(max_length=240)
    brand = models.CharField(max_length=240)
    #FOR WHEN WE HAVE IMAGE UPLOADS>> picture = models.ImageField(upload_to=None, height_field=None, width_fielmax_length=100)
    price = models.CharField(max_length=240)
    size = models.CharField(max_length=240)
    rms = models.CharField(max_length=240)
    peak = models.CharField(max_length=240)
    description = models.CharField(max_length=500)
    reviews = models.ForeignKey('Review', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sub(models.Model):
    name = models.CharField(max_length=240)
    brand = models.CharField(max_length=240)
    #FOR WHEN WE HAVE IMAGE UPLOADS>> picture = models.ImageField(upload_to=None, height_field=None, width_fielmax_length=100)
    size = models.CharField(max_length=240)
    rms = models.CharField(max_length=240)
    peak = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class AmpPost(models.Model):
    name = models.CharField(max_length=240)
    brand = models.CharField(max_length=240)
    #FOR WHEN WE HAVE IMAGE UPLOADS>> picture = models.ImageField(upload_to=None, height_field=None, width_fielmax_length=100)
    price = models.CharField(max_length=240)
    wattage = models.CharField(max_length=240)
    description = models.CharField(max_length=500)
    reviews = models.ForeignKey('Review', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Amp(models.Model):
    name = models.CharField(max_length=240)
    brand = models.CharField(max_length=240)
    #FOR WHEN WE HAVE IMAGE UPLOADS>> picture = models.ImageField(upload_to=None, height_field=None, width_fielmax_length=100)
    wattage = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    body = models.CharField(max_length=500)
    rating = models.IntegerField()

    def __str__(self):
        return self.title