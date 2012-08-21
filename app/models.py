from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Extension of the basic Django User
    """
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=255, blank=True, null=True, default="")

    def __unicode__(self):
        return "%s" % self.user

class Article(models.Model):
    title = models.CharField(max_length=255, null=False, default="Default title")
    text = models.CharField(max_length=10000, null=False, default="Default text")
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
