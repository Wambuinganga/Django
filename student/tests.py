from django.test import TestCase
from .models import Student
import datetime
from .forms import StudentForm



class StudentTestCase(TestCase):
    def setUp(self):
        self.student=Student(
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

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())

    # def test_age_above_18(self):
    #    self.assertFalse(self.student.clean() < 18)
    # def test_age_below_30(self):
    #    self.assertFalse( self.student.clean() > 30)


#setting up some data to ensure that every time the student is registered, the data is always correct and valid
class CreateStudentTestCase(TestCase):
    def setUp(self):
        self.data={
            'first_name':'Wambui',
            'last_name':'Nganga',
            'date_of_birth':datetime.date(1997, 10, 20),
            'registration_number':'SCP213-0079/2017',
            'place_of_residence':' Nairobi',
            'phone_number':'079876543',
            'email':'peshys@gmail.com',
            'guardian_phone':'079876543',
            'id_number':234567890,
            'date_joined':datetime.date.today(),
        
            }
        self.bad_data={
            'first_name':'Wambui',
            'last_name':'Nganga',
            'date_of_birth':'long time ago',
            'registration_number':'SCP213-0079/2017',
            'place_of_residence':' Nairobi',
            'phone_number':'079876543',
            'email':'',
            'guardian_phone':'079876543',
            'id_number':234567890,
            'date_joined':datetime.date.today(),

        }

    def test_student_form_accepts_valid_data(self):
        form=StudentForm(self.data)
        self.assertTrue(form.is_valid())

    def test_student_form_rejects_invalid_data(self):
        form=StudentForm(self.bad_data)
        self.assertFalse(form.is_valid())






# Create your tests here.
