from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import transaction
from django.contrib.auth import get_user_model

from .models import Activation
from .views.activation import send_activation_email

AuthUserModel = get_user_model()


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(sender, instance, **kwargs):
    print("\nSignal pre_save was triggerd!\n")

    if not instance.pk:
        instance.is_active = False
        instance.password = None


@receiver(post_save, sender=AuthUserModel)
def create_activation(sender, instance, created, **kwargs):
    print("\nSignal post_save was triggerd!\n")
    try:
        with transaction.atomic():
            if created:
                Activation(user=instance).save()
                send_activation_email(instance)
    except ValueError:
        AuthUserModel.objects.get(pk=instance.id).delete()
