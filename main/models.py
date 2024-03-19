from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class todo(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/todo/page/{self.id}'
    

class Profile(models.Model):

    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE, verbose_name='')
    avatar = models.ImageField(verbose_name='аватар',blank=True,null=True, upload_to='photos/%Y/%m/%d')
    bio = models.TextField(verbose_name='О себе' ,blank=True,null=True)

    def __str__(self):
        if self.user:
            return str(self.user.id)#, f'профиль-{self.id}',f'создатель-{self.user.username}'
        else:
            return 'ты хуесос'
    def get_absolute_url(self):
        return f'/todo/profile/{self.id}'