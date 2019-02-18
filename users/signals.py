from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User as DjangoUser
from django.db.models.signals import post_save
from users.models import User


@receiver(signal=post_save, sender=DjangoUser)
def create_userprofile(sender, instance, signal, created, *args, **kwargs):
    if created:
        User.objects.create(profile=instance)

    # instance.profile.save()



@receiver(signal=post_save)
def save_newmessage(instance, signal, *args, **kwargs):
    instance.profile.save()


post_save.connect(save_newmessage)
post_save.connect(create_userprofile, sender=DjangoUser)