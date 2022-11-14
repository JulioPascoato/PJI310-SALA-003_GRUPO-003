# @receiver(post_save, sender=Professor)
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Professor


def novoProfessor(sender, instance, created, **kwargs):
    if created:
        user = instance
        professor = Professor.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            nome=user.first_name
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(novoProfessor, sender=User)
post_delete.connect(deleteUser, sender=Professor)
