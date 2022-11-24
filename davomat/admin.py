from django.contrib import admin
from .models import CourseTime, Davomat, Pupil, Course,Teacher,Group
# Register your models here.


class DavomatAdmin(admin.ModelAdmin):
      # search_fields = ('group__title',)
      # search_help_text = 'Faqat o\'quvchi ismi bo\'yicha qidiring.!'
      # list_filter = ['date', 'active', 'group__course']
      # list_display=['teacher','id', 'date','active','get_teacher','get_course',]
      # list_display_links=['teacher','id']
      date_hierarchy='date'
      

      # def get_teacher(self,obj):
      #       return obj.teacher.teacher

      # def get_course(self,obj):
      #       return obj.group.course.title

class PupilAdmin(admin.ModelAdmin): 
      filter_horizontal=['course',]




      
admin.site.register(Davomat,DavomatAdmin)
admin.site.register(Pupil,PupilAdmin)
admin.site.register(Course)
admin.site.register(CourseTime)
admin.site.register(Teacher)
admin.site.register(Group)
