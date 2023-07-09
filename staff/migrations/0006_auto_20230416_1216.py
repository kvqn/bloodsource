# Generated by Django 4.1.7 on 2023-04-16 12:16

from django.db import migrations
from django.contrib.auth import get_user_model
from datetime import datetime

def add_users(apps, schema_editor):
    Profile = apps.get_model('users', 'Profile')
    Staff = apps.get_model('staff', 'Staff')
    Clinic = apps.get_model('staff', 'Clinic')
    User = get_user_model()

    user = Profile.objects.create(username='rashmi', password="rashmi", first_name="Rashmi", last_name="Verma", email="rashmi@gmail.com", phone="90133382482",
        blood_group="B-", state="Delhi", city="New Delhi", pincode=110089, date_of_birth="2003-06-15", weight=55)

    clinic = Clinic.objects.get(clinic_id=11)
    staff = Staff.objects.create(user_id=user, clinic_id=clinic)

    user = User.objects.get(username='rashmi')
    user.set_password('rashmi')
    user.save()

    user = Profile.objects.create(username='mainak', password="mainak", first_name="Mainak", last_name="Gangopadhyay", email="mainak@gmail.com", phone="90133384242",
        blood_group="AB-", state="Delhi", city="New Delhi", pincode=110039, date_of_birth="2002-10-12", weight=55, is_staff=True)

    clinic = Clinic.objects.get(clinic_id=12)
    staff = Staff.objects.create(user_id=user, clinic_id=clinic)

    user = User.objects.get(username='mainak')
    user.set_password('mainak')
    user.save()

    user = Profile.objects.create(username='soumya', password="soumya", first_name="Soumya", last_name="Verma", email="soumya@gmail.com", phone="912233382482",
                                  blood_group="B+", state="Maharashtra", city="Mumbai", pincode=400007, date_of_birth="2001-05-12", weight=55)

    clinic = Clinic.objects.get(clinic_id=38)
    staff = Staff.objects.create(user_id=user, clinic_id=clinic)

    user = User.objects.get(username='soumya')
    user.set_password('soumya')
    user.save()

    user = Profile.objects.create(username='souvik', password="souvik", first_name="Souvik", last_name="Sharma", email="souvik@gmail.com", phone="901123382482",
                                    blood_group="A+", state="Rajasthan", city="Jaipur", pincode=342001, date_of_birth="2000-04-11", weight=74)

    clinic = Clinic.objects.get(clinic_id=52)
    staff = Staff.objects.create(user_id=user, clinic_id=clinic)

    user = User.objects.get(username='souvik')
    user.set_password('souvik')
    user.save()

    user = Profile.objects.create(username='harsh' , password="harsh", first_name="Harsh", last_name="Verma", email="h_verma@gmail.com", phone="99133382482",
                                    blood_group="O+", state="Delhi", city="New Delhi", pincode=110089, date_of_birth="1999-03-10", weight=65)

    user = User.objects.get(username='harsh')
    user.set_password('harsh')
    user.save()

    user = Profile.objects.create(username='1001volts', password="1001volts", first_name="Pranav", last_name="Verma", email="1001volts@gmail.com", phone="912382482",
                                    blood_group="A-", state="Delhi", city="New Delhi", pincode=110078, date_of_birth="2002-10-05", weight=70)

    user = User.objects.get(username='1001volts')
    user.set_password('1001volts')
    user.save()

    user = Profile.objects.create(username='dt1', password="dt1", first_name="Divyansh", last_name="Tanwar", email="dt1@gmailc.om", phone="94258382482",
                                    blood_group="B+", state="Delhi", city="New Delhi", pincode=110070, date_of_birth="2003-06-15", weight=78)

    user = User.objects.get(username='dt1')
    user.set_password('dt1')
    user.save()

    user = Profile.objects.create(username='himanshu', password="himanshu", first_name="Himanshu", last_name="Sharma", email="zenocres@gmail.com", phone="9128182482",
                                    blood_group="O-", state="Delhi", city="New Delhi", pincode=110034, date_of_birth="2003-05-15", weight=65)

    user = User.objects.get(username='himanshu')
    user.set_password('himanshu')
    user.save()

    user = Profile.objects.create(username='jichris', password="jichris", first_name="Kisna", last_name="Anand", email="jich@gmail.com", phone="91243282482",
                                    blood_group="AB-", state="Delhi", city="New Delhi", pincode=110081, date_of_birth="2002-10-15", weight=65)

    user = User.objects.get(username='jichris')
    user.set_password('jichris')
    user.save()

    user = Profile.objects.create(username='johndoe', password="johndoe", first_name="John", last_name="Doe", email="johnny@gmail.com", phone="91232482482",
                                    blood_group="B-", state="Delhi", city="New Delhi", pincode=110081, date_of_birth="2002-11-15", weight=65)

    user = User.objects.get(username='johndoe')
    user.set_password('johndoe')
    user.save()

    user = Profile.objects.create(username='jayant', password="jayant", first_name="Jayant", last_name="Singh", email="jay@gmail.com", phone="91232242482",
                                    blood_group="O+", state="Delhi", city="New Delhi", pincode=110017, date_of_birth="2002-04-04", weight=65)

    user = User.objects.get(username='jayant')
    user.set_password('jayant')
    user.save()




def add_appointments(apps, schema_editor):
    Appointment = apps.get_model('staff', 'Appointment')
    User = apps.get_model('users', 'Profile')
    Clinic = apps.get_model('staff', 'Clinic')

    Appointment.objects.create(user_id=User.objects.get(username='1001volts'), clinic_id=Clinic.objects.get(clinic_id=38), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='dt1'), clinic_id=Clinic.objects.get(clinic_id=52), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='himanshu'), clinic_id=Clinic.objects.get(clinic_id=10), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='jichris'), clinic_id=Clinic.objects.get(clinic_id=10), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='johndoe'), clinic_id=Clinic.objects.get(clinic_id=10), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='jayant'), clinic_id=Clinic.objects.get(clinic_id=10), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='johndoe'), clinic_id=Clinic.objects.get(clinic_id=11), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='jayant'), clinic_id=Clinic.objects.get(clinic_id=11), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='johndoe'), clinic_id=Clinic.objects.get(clinic_id=11), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='jayant'), clinic_id=Clinic.objects.get(clinic_id=12), type='Donor', datetime_of_appointment='2023-04-16')
    Appointment.objects.create(user_id=User.objects.get(username='johndoe'), clinic_id=Clinic.objects.get(clinic_id=12), type='Donor', datetime_of_appointment='2023-04-16')


    # Appointment.objects.create(user_id=User.objects.get(username='1001volts'), clinic_id=Clinic.objects.get(clinic_id=38), type='Donor', datetime_of_appointment=datetime(2023, 4, 16, 5, 12, 0))
    # Appointment.objects.create(user_id=User.objects.get(username='dt1'), clinic_id=Clinic.objects.get(clinic_id=52), type='Donor', datetime_of_appointment=datetime(2023, 4, 16, 6, 12, 0))
    # Appointment.objects.create(user_id=User.objects.get(username='himanshu'), clinic_id=Clinic.objects.get(clinic_id=10), type='Donor', datetime_of_appointment=datetime(2023, 4, 16, 21, 12, 0))
    # Appointment.objects.create(user_id=User.objects.get(username='jichris'), clinic_id=Clinic.objects.get(clinic_id=10), type='Donor', datetime_of_appointment=datetime(2023, 4, 16, 22, 12, 0))
    # Appointment.objects.create(user_id=User.objects.get(username='johndoe'), clinic_id=Clinic.objects.get(clinic_id=10), type='Donor', datetime_of_appointment=datetime(2023, 4, 16, 00, 12, 0))
    # Appointment.objects.create(user_id=User.objects.get(username='jayant'), clinic_id=Clinic.objects.get(clinic_id=11), type='Donor', datetime_of_appointment=datetime(2023,4,16,2,12,0))
    # Appointment.objects.create(user_id=User.objects.get(username='johndoe'), clinic_id=Clinic.objects.get(clinic_id=11), type='Donor', datetime_of_appointment=datetime(2023, 4, 16, 3, 12, 0))
    # Appointment.objects.create(user_id=User.objects.get(username='jayant'), clinic_id=Clinic.objects.get(clinic_id=12), type='Donor', datetime_of_appointment=datetime(2023, 4, 16, 4, 12, 0))
    # Appointment.objects.create(user_id=User.objects.get(username='jayant'), clinic_id=Clinic.objects.get(clinic_id=12), type='Donor', datetime_of_appointment=datetime(2023, 4, 16, 4, 12, 0))
    # Appointment.objects.create(user_id=User.objects.get(username='johndoe'), clinic_id=Clinic.objects.get(clinic_id=12), type='Donor', datetime_of_appointment=datetime(2023, 4, 16, 5, 12, 0))








class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20230416_1201'),
    ]

    operations = [
        migrations.RunPython(add_users),
        migrations.RunPython(add_appointments),
    ]