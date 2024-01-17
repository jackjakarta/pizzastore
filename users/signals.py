from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(sender, instance, **kwargs):
    print("\nSignal pre_save was triggerd!\n")

    if not instance.pk:
        instance.is_active = False
        instance.password = None
