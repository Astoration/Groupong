from django.contrib import admin
from .models import Post
#from .models import Profile
from .models import Comment
#from groupong.models import Profile
 
#class ProfileInline(admin.StackedInline):
#    model = Profile
#    can_delete = False
#    verbose_name_plural = 'profile'
	
admin.site.register(Post)
# admin.site.register(Profile)
admin.site.register(Comment)