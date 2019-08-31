from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,)
    bio = models.TextField(max_length=800, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_author_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_author_profile(sender, instance, **kwargs):
    instance.author.save()


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE,)
    description = models.CharField(max_length=400)
    time_required = models.IntegerField()
    instructions = models.TextField()

    def __str__(self):
        return self.title
