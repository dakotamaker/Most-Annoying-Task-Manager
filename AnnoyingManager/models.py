from django.db import models
from django.core.validators import validate_email, RegexValidator, MaxValueValidator, MinValueValidator
from datetime import datetime
import uuid


class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user_name = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=255, blank=False, unique=True, validators=[validate_email])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)


class Task(models.Model):
    task_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.CharField(max_length=255)
    done = models.BooleanField(default=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Could have used a different DB but I wanted to just stick with sqlite for convenience, but they don't have support
    # for storing datetime values, so I went with integer values for ease of comparing
    due_date = models.IntegerField(default=int(datetime.now().timestamp()), blank=True)

