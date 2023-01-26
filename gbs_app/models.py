from django.db import models


# Create your models here.
class userlogin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    u_type = models.CharField(max_length=225)

class user_details(models.Model):
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    mobile_no = models.IntegerField()
    usertype = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    u_password = models.CharField(max_length=255)

class staff_details(models.Model):
    s_name = models.CharField(max_length=25)
    s_address = models.CharField(max_length=100)
    s_ph_no = models.IntegerField()
    s_email = models.CharField(max_length=50)
    s_passwd = models.CharField(max_length=25)

class feedback(models.Model):
    user_name = models.CharField(max_length=25)
    ph_no = models.IntegerField()
    feedback = models.CharField(max_length=120)

class feedback_response(models.Model):
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    response = models.CharField(max_length=120)


class gasrefill_booking(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    cylinder = models.CharField(max_length=100)




