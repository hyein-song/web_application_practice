from django.contrib import admin
from accounts.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Comment)

