from django.contrib import admin
from. models import Post
from theblog.models import Score, Comment, Contact

# Register your models here.
admin.site.register(Post)
admin.site.register(Score)
admin.site.register(Comment)
admin.site.register(Contact)