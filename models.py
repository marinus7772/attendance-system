from django.db import models
from groups_app.models import Student
from schedules.models import Schedule

class Attendance(models.Model):

    STATUS_CHOICES = (
        ('present', 'Присутствовал'),
        ('absent', 'Отсутствовал'),
        ('late', 'Опоздал'),
        ('excused', 'Уважительная причина'),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    late_minutes = models.IntegerField(
        default=0
    )

    reason = models.TextField(blank=True)

    lesson_topic = models.TextField(blank=True)

    homework = models.TextField(blank=True)

    marked_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student} - {self.date}"


class ExcuseRequest(models.Model):

    attendance = models.ForeignKey(
        Attendance,
        on_delete=models.CASCADE
    )

    comment = models.TextField()

    document = models.ImageField(
        upload_to='documents/'
    )

    approved = models.BooleanField(
        null=True,
        blank=True
    )

    teacher_comment = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class QRSession(models.Model):

    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE
    )

    code = models.CharField(max_length=255)

    expires_at = models.DateTimeField()

    @property
    def excuserequest(self):
        try:
            return self.excuserequest_set.first()
        except:
            return None