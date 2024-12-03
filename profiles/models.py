from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import io
import base64

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', unique=True)
    photo = models.BinaryField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if hasattr(self, '_uploaded_photo'):
            img = Image.open(self._uploaded_photo)
            img = img.convert("RGB") 
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=85)  
            self.photo = img_io.getvalue()
        super().save(*args, **kwargs)

    def set_photo(self, uploaded_file):
        self._uploaded_photo = uploaded_file

    def get_photo_url(self):
        if self.photo:
            encoded_photo = base64.b64encode(self.photo).decode('utf-8')
            return f"data:image/jpeg;base64,{encoded_photo}"
        return None

    def __str__(self):
        return f"Profile of {self.user.username}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
