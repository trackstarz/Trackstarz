from django.contrib import admin
from blog.models import Burst, Category, Comment, Reply, BurstLike, CommentLike, ReplyLike

admin.site.register(Burst)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(BurstLike)
admin.site.register(CommentLike)
admin.site.register(ReplyLike)

# Register your models here.
