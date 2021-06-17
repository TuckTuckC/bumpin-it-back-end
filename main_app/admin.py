from django.contrib import admin
from .models import (User, Amp, Post, Sub, Review)

# Register your models here.
admin.site.register(User)
admin.site.register(Amp)
admin.site.register(Post.SubPost)
admin.site.register(Post.AmpPost)
admin.site.register(Sub)
# admin.site.register(SubPost)
admin.site.register(Review)