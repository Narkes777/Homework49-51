from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import hjjg

@receiver(post_save, sender=User)
def ppp(sender, *args, **kwargs):
    if kwargs['created']:
        ss = hjjg.objects.create(name=kwargs['instance'])






