from django.contrib import admin
from .models import Attendance, ExcuseRequest, QRSession

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'schedule', 'date', 'status', 'marked_at')
    list_filter = ('status', 'date')
    search_fields = ('student__user__first_name', 'student__user__last_name')

@admin.register(ExcuseRequest)
class ExcuseRequestAdmin(admin.ModelAdmin):
    list_display = ('attendance', 'approved', 'created_at')
    list_filter = ('approved',)

@admin.register(QRSession)
class QRSessionAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'code', 'expires_at')