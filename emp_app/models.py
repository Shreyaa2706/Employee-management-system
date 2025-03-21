from django.db import models


# Create your models here.
class department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class employee(models.Model):
    objects = None
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20)
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.phone)
