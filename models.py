from django.db import models


# Create your models here.

opt1 = 'Kasargod'
opt2 = 'Kannur'
opt3 = 'Wayanad'
opt4 = 'Kozhikode'
opt5 = 'Malappuram'
opt6 = 'Palakkad'
opt7 = 'Thrissur'
opt8 = 'Ernakulam'
opt9 = 'Kottayam'
opt10 = 'Kollam'
opt11 = 'Aalappuzha'
opt12 = 'Idukki'
opt13 = 'Pathanamthitta'
opt14 = 'Trivandrum'

district_options = [(opt1,opt1),(opt2,opt2), (opt3,opt3),  (opt4,opt4), (opt5,opt5), (opt6,opt6), (opt7,opt7), (opt8,opt8), (opt9,opt9), (opt10,opt10), (opt11,opt11), (opt12,opt12), (opt13,opt13), (opt14,opt14)]

class studform(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    college = models.CharField(max_length=40)
    place = models.CharField(max_length=40)
    district = models.CharField(max_length=30, choices=district_options)
    phone = models.IntegerField()
    email = models.EmailField()
    
