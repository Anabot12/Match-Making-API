from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    person1 = models.CharField(max_length=1000, default='some string')
    person2 = models.CharField(max_length=100, default='some string')
    name = models.CharField(max_length=255, default='some string')
    tags = models.CharField(max_length=1000, default='some string')

    def __str__(self):
        return self.name

    @staticmethod
    def save_person_details(person_details):
        person1 = person_details.get('person1')
        person2 = person_details.get('person2')
        name = person_details.get('name')
        tags = person_details.get('tags')

        person = Profile.objects.create(name=name, tags=tags)
        return person


class Swipe(models.Model):
    swiper = models.ForeignKey(User, related_name='swipes', on_delete=models.CASCADE)
    liked_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('swiper', 'liked_profile')
