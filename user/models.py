import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Department(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class User(AbstractUser, BaseModel):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )
    EMPLOYMENT_TYPE = (
        ('full_time', 'full_time'),
        ('part_time', 'part_time'),
        ('contract', 'contract'),
    )

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='users', null=True)
    address = models.TextField()
    job_title = models.CharField(max_length=250)
    joined_date = models.DateField(null=True)
    salary = models.PositiveBigIntegerField(default=0)
    gender = models.CharField(max_length=250, choices=GENDER)
    date_of_birth = models.DateField(null=True)
    employment_type = models.CharField(max_length=250, choices=EMPLOYMENT_TYPE)
    contact = models.CharField(max_length=50)
    note = models.TextField()
    profile_image = models.ImageField(upload_to='user/profile_image', null=True, blank=True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + self.last_name