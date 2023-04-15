# Generated by Django 4.1.7 on 2023-04-14 21:41

from django.db import migrations

SQL_QUERIES = """
insert into users_profile values(5,'Monika',NULL,0,'monika',1,'2023-04-15 09:10:15.000000','Monika','M','monika@gmail.com','9013075758','O+','Delhi','New Delhi',110089,'2023-04-15',55,'2003-06-15',0);
insert into users_profile values(6,'Guneet',NULL,0,'kevqn',1,'2023-04-15 09:11:15.000000','Guneet','Aggarwal','guneet@gmail.com','9754366341','O+','Delhi','New Delhi',110010,'2023-04-15',49,'2003-06-15',0);
insert into users_profile values(7,'Ram',NULL,0,'ram_a',1,'2023-04-15 09:12:15.000000','Ram','Aggarwal','ram@yahoo.com','9754366311','A-','Delhi','New Delhi',110029,'2023-04-15',79,'2000-12-09',0);
insert into users_profile values(8,'Shyam',NULL,0,'shyam',1,'2023-04-15 09:13:15.000000','Shyam','Meena','shyam@gmail.com','9752966341','B+','Delhi','New Delhi',110090,'2023-04-15',56,'2003-01-06',0);
insert into users_profile values(9,'Rahul',NULL,0,'rahul',1,'2023-04-15 09:14:15.000000','Rahul','Dhawan','rahul@rediffmail.com','9323496341','AB+','Maharashtra','Mumbai',4000007,'2023-04-15',49,'2003-03-29',0);
insert into users_profile values(10,'Japneet',NULL,0,'jappi',1,'2023-04-15 09:15:15.000000','Japneet','Singh','japneet@gmail.com','9754366341','O+','Rajasthan','Alwar',301001,'2023-04-15',75,'2003-06-15',0);
"""

class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20230414_2120'),
    ]

    operations = [
        migrations.RunSQL(SQL_QUERIES),
    ]