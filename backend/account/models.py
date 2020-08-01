from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from core.kafkaClient import Producer
import pdb

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        new_user_profile = UserProfile(user=instance)
        new_user_profile.save()
        from account.api.serializers import UserProfileSerializer
        producer = Producer()
        data_user_profile = UserProfileSerializer(new_user_profile).data
        data_user_profile['event_type'] = "new user"
        producer.send(data_user_profile)
