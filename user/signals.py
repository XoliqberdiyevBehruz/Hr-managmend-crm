from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from user import models 
from common.models import Payment

@receiver(post_save, sender=models.User)
def create_payment_for_user(sender, instance, *args, **kwargs):
    payment, created = Payment.objects.get_or_create(employee=instance, status='unpaid', salary=instance.salary) 
    print('payment created successfully')