from django.db import models

# Create your models here.
class Name(models.Model):
    fullname = models.CharField(max_length=45)
    age = models.IntegerField(max_length=2)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.fullname
    def getEmail(self):
        return self.email
    def getAge(self):
        return self.age

class Status(models.Model):
    position = {
        "Software": "Engineer",
        "Website": "Developer",
        "Student": "College/High School"
    }

    def __str__(self):
        return

