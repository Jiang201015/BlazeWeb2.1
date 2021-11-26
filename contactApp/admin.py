from django.contrib import admin
from .models import Ad
from django.utils.safestring import mark_safe
from .models import Resume
# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'personID', 'birth', 'edu', 'position', 'image_data')

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="120px" />' % obj.photo.url)

    image_data.short_description = u'头像照片'


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Ad)
