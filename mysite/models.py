from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='profile_photo/', blank=True, default='profile_photo/sea_side.jpeg')
    bio = models.CharField(max_length=265, blank=True)
    contact_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        db_table = 'profile'


class Projects(models.Model):
    image = models.ImageField(upload_to='project_folder')
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='1')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return f'{self.profile.user.username}'

    class Meta:
        db_table = 'projects'
        ordering = ['-post_date']

    @classmethod
    def get_projects(cls):
        project = cls.objects.all()
        return project
