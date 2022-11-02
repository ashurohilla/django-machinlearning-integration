from django.contrib import admin
from projects.models import hardware, project 
from  embed_video.admin  import  AdminVideoMixin
class projectAdmin(admin.ModelAdmin):
    list_display =('Project_name','project_images','project_id','project_date','project_heading','project_half','project_blogimage', 'project_video','project_content')
admin.site.register(project,projectAdmin)    

class hardwareAdmin(admin.ModelAdmin):
     list_display =('Project_name','project_images','project_id','project_date','project_heading','project_half','project_blogimage', 'project_video','project_content')

admin.site.register(hardware,hardwareAdmin) 