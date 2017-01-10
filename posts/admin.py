from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","timestamp","updated"]
	list_display_links = ["title","updated","timestamp"]
	list_filter=["updated","timestamp"]
	search_fields =["title","content"]
	list_editable=[]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
