from django.db import models

from user.models import BaseModel


class Platform(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    STATUS = (
        ('closed', 'closed'),
        ('active', 'active')
    )
    
    job_title = models.CharField(max_length=250)
    short_description = models.CharField(max_length=250)
    full_description = models.TextField()
    platforms = models.ManyToManyField('Platform', related_name='vacancies')
    post_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS, default='active')

    def __str__(self):
        return self.job_title
    


class JobApplication(BaseModel):
    STATUS = (
        ('pending', 'pending'),
        ('reviewed', 'reviewed'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    )

    name = models.CharField(max_length=250)
    contact = models.EmailField()
    apllied_from = models.CharField(max_length=250)
    date = models.DateField()
    status = models.CharField(max_length=250, choices=STATUS)

    def __str__(self):
        return self.name


class Payment(BaseModel):
    STATUS = (
        ('paid', 'paid'),
        ('unpaid', 'unpaid'),
    )
    status = models.CharField(max_length=250, choices=STATUS)
    employee = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, related_name='payments')
    salary = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.status} {self.employee} {self.salary}'
