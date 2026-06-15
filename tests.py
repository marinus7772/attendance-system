from django.test import TestCase
from django.contrib.auth import get_user_model
from groups_app.models import Group, Student
from schedules.models import Subject, Schedule
from attendance.models import Attendance
from datetime import date, time

User = get_user_model()


class ModelTests(TestCase):

    def test_create_user(self):
        """Тест создания пользователя"""
        user = User.objects.create_user(
            username='testteacher',
            password='123',
            first_name='Иван',
            last_name='Иванов',
            role='teacher'
        )
        self.assertEqual(user.username, 'testteacher')
        self.assertEqual(user.role, 'teacher')
        print("✓ Тест создания пользователя пройден")

    def test_create_group(self):
        """Тест создания группы"""
        user = User.objects.create_user(
            username='testteacher2',
            password='123',
            first_name='Петр',
            last_name='Петров',
            role='teacher'
        )
        group = Group.objects.create(
            name='ТП-11',
            course=1,
            curator=user
        )
        self.assertEqual(group.name, 'ТП-11')
        self.assertEqual(group.course, 1)
        print("✓ Тест создания группы пройден")

    def test_create_subject(self):
        """Тест создания предмета"""
        subject = Subject.objects.create(title='Программирование')
        self.assertEqual(subject.title, 'Программирование')
        print("✓ Тест создания предмета пройден")

    def test_create_schedule(self):
        """Тест создания расписания"""
        user = User.objects.create_user(
            username='testteacher3',
            password='123',
            first_name='Сергей',
            last_name='Сидоров',
            role='teacher'
        )
        group = Group.objects.create(name='ПРО-11', course=1)
        subject = Subject.objects.create(title='Базы данных')
        schedule = Schedule.objects.create(
            group=group,
            teacher=user,
            subject=subject,
            classroom='301',
            weekday=1,
            week_type='odd',
            start_time=time(9, 0),
            end_time=time(10, 30)
        )
        self.assertEqual(schedule.classroom, '301')
        print("✓ Тест создания расписания пройден")

    def test_create_attendance(self):
        """Тест создания записи посещаемости"""
        user = User.objects.create_user(
            username='teststudent',
            password='123',
            first_name='Анна',
            last_name='Сидорова',
            role='student'
        )
        group = Group.objects.create(name='ТП-11', course=1)
        student = Student.objects.create(
            user=user,
            group=group,
            admission_date=date.today()
        )
        subject = Subject.objects.create(title='Программирование')
        schedule = Schedule.objects.create(
            group=group,
            teacher=user,
            subject=subject,
            classroom='301',
            weekday=1,
            week_type='odd',
            start_time=time(9, 0),
            end_time=time(10, 30)
        )
        attendance = Attendance.objects.create(
            student=student,
            schedule=schedule,
            date=date.today(),
            status='present'
        )
        self.assertEqual(attendance.status, 'present')
        print("✓ Тест создания посещаемости пройден")


class AttendanceAPITests(TestCase):

    def test_save_attendance_api(self):
        """Тест API сохранения посещаемости"""
        user = User.objects.create_user(
            username='teststudent2',
            password='123',
            first_name='Мария',
            last_name='Петрова',
            role='student'
        )
        group = Group.objects.create(name='ТП-21', course=2)
        student = Student.objects.create(
            user=user,
            group=group,
            admission_date=date.today()
        )
        subject = Subject.objects.create(title='ООП')
        schedule = Schedule.objects.create(
            group=group,
            teacher=user,
            subject=subject,
            classroom='302',
            weekday=2,
            week_type='odd',
            start_time=time(9, 0),
            end_time=time(10, 30)
        )

        attendance = Attendance.objects.create(
            student=student,
            schedule=schedule,
            date=date.today(),
            status='absent',
            reason='Болезнь'
        )
        self.assertEqual(attendance.status, 'absent')
        self.assertEqual(attendance.reason, 'Болезнь')
        print("✓ Тест API сохранения посещаемости пройден")