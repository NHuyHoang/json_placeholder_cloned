from django.contrib import admin
from .models.user import User
from .models.company import Company
from .models.staff import Staff
from .models.comment import Comment
from .models.post import Post
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Company)
admin.site.register(Staff)
admin.site.register(Post)
admin.site.register(Comment)
