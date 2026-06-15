from django.urls import path
from .views import (
    dashboard, schedule_page, attendance_page,
    reports_page, notifications_page, custom_logout,
    save_attendance, mark_all_present,
    create_excuse_request, process_excuse_request,
    mark_attendance_by_qr, attendance_stats_api,
    attendance_journal,
    export_student_report_excel,
    export_group_report_excel, export_teacher_report_excel,
    export_summary_report_excel
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('schedule/', schedule_page, name='schedule'),
    path('attendance/', attendance_page, name='attendance'),
    path('attendance-journal/', attendance_journal, name='attendance_journal'),
    path('reports/', reports_page, name='reports'),
    path('notifications/', notifications_page, name='notifications'),
    path('logout/', custom_logout, name='logout'),

    # AJAX endpoints
    path('api/save-attendance/', save_attendance, name='save_attendance'),
    path('api/mark-all-present/', mark_all_present, name='mark_all_present'),
    path('api/attendance-stats/', attendance_stats_api, name='attendance_stats_api'),

    # QR-код отметка
    path('mark-attendance/<int:schedule_id>/', mark_attendance_by_qr, name='mark_attendance_by_qr'),

    # Уведомления
    path('api/create-excuse-request/', create_excuse_request, name='create_excuse_request'),
    path('api/process-request/<int:request_id>/<str:action>/', process_excuse_request, name='process_excuse_request'),

    # Отчеты Excel
    path('report/student/excel/<int:student_id>/', export_student_report_excel, name='report_student_excel'),
    path('report/group/excel/<int:group_id>/', export_group_report_excel, name='report_group_excel'),
    path('report/teacher/excel/', export_teacher_report_excel, name='report_teacher_excel'),
    path('report/summary/excel/', export_summary_report_excel, name='report_summary_excel'),
]