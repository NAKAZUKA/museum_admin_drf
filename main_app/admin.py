from django.contrib import admin
from .models import Post, Answer, Question, Exhibit


admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Exhibit)
