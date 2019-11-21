from django.test import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher
import datetime



class StudentCourseTeacherTestCase(TestCase):
    def setUp(self):
        self.student_a=Student.objects.create(
            first_name='Wambui',
            last_name='Nganga',
            date_of_birth=datetime.date(1997, 10, 20),
            registration_number='SCP213-0079/2017',
            place_of_residence=' Nairobi',
            phone_number='079876543',
            email='peshys@gmail.com',
            guardian_phone='079876543',
            id_number=234567890,
            date_joined=datetime.date.today(),
            )
        self.student_b=Student.objects.create(
            first_name='Julianna',
            last_name='Wanjiru',
            date_of_birth=datetime.date(1997, 10, 20),
            registration_number='SCP213-0079/2017',
            place_of_residence=' Nairobi',
            phone_number='079876543',
            email='shiro@gmail.com',
            guardian_phone='079876543',
            id_number=234567890,
            date_joined=datetime.date.today(),
            )
        self.python=Course.objects.create(
            name='Python',
            duration_in_months= 9,
            course_number=101,
            description='lorem ipsum dofvbdnmiuytreadx hgjyuinms',

            )
        self.javascript=Course.objects.create(
            name='Javascript',
            duration_in_months= 9,
            course_number=202,
            description='lorem ipsum dofvbdnmiuytreadx hgjyuinms',
            )
        self.hardware=Course.objects.create(
            name='Hardware',
            duration_in_months= 9,
            course_number=404,
            description='lorem ipsum dofvbdnmiuytreadx hgjyuinms',
            )
        self.teacher_a=Teacher.objects.create(
            first_name='Mwalimu',
            last_name='Teacher',
            id_number=345678,
            registration_number='XOXO124',
            place_of_residence='Nairobi',
            phone_number='07987654',
            email='mwalimu@teacher.com',
            date_joined=datetime.date.today(),
            profession='Mwalimu',
            )
        self.teacher_b=Teacher.objects.create(
            first_name='Monseur',
            last_name='Frau',
            id_number=345678,
            registration_number='XOXO124',
            place_of_residence='Nairobi',
            phone_number='07987654',
            email='frau@mons.com',
            date_joined=datetime.date.today(),
            profession='Frau',
            )
    def test_student_can_join_many_courses(self):
        self.assertEqual(self.student_a.courses.count(), 0)
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(), 1)
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student_a.courses.count(), 2)
        self.student_a.courses.add(self.hardware)
        self.assertEqual(self.student_a.courses.count(), 3)

    def test_course_can_have_many_students(self):
        self.python.students.add(self.student_a, self.student_b) 
        self.assertEqual(self.python.students.count(), 2)

    def test_teacher_can_have_many_courses(self):
        self.teacher_a.courses.add(self.python, self.hardware, self.javascript) 
        self.assertEqual(self.teacher_a.courses.count(), 3)

    def test_course_teacher_cannot_have_many_teachers(self):
        self.python.teacher=self.teacher_a # assigning a teacher to a course
        self.assertEqual(self.teacher.python.first_name, 'Mwalimu') #testing that the course is assigned to teacher_a
        self.hardware.teacher=self.teacher_b #reassigning the course to a teacher
        self.assertEqual(self.teacher.hardware.first_name, 'Monseur')

    def test_course_teacher_is_in_student_teachers_list(self):
       self.python.teacher=self.teacher_b #create a teacher for a course
       self.student_a.courses.add(self.python)#assign teacher to te course
       teachers=self.student_a.teachers#create a list for students_a teachers
       self.assertTrue(self.teacher_b in teachers())#check if assigned teacher is among them


        







        # The .students is because of the relationship and we gave the name to use at models
        
