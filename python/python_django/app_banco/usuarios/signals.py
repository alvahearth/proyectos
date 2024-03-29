from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Profile, Dinero, MoverDinero

@receiver(post_save, sender=CustomUser)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Dinero.objects.create(user=instance)
        MoverDinero.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def actualizar_perfil(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
        instance.dinero.save()
        instance.moverdinero.save()
        
        
