from django.db import models

# Create your models here.
class GeneralInfo(models.Model):
    '''Not '''
    name = models.CharField(max_length=250)
    bio = models.TextField(default="text")
    gender = models.CharField(max_length=6, default="text")
    occupation = models.CharField(max_length=250, default = "text")
    # socials
    fb_link = models.URLField(default = "text")
    ig_link = models.URLField(default = "text")
    linkedIn_link = models.URLField(default = "text")
    x_link = models.URLField(default = "text")
    
    def __str__(self):
        return self.name
        # return f"Name - {self.name}"
        
        
class Profile(models.Model):
    GenderChoice = [
        ('Male','Male'),
        ('Female','Female')
    ]
    name = models.CharField(max_length=250)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=GenderChoice, max_length=7)
    address = models.CharField(max_length=400, blank=True,null=True)
    '''update model-add work_place'''
    occupation = models.CharField(max_length=250)
    work_place = models.CharField(max_length=250,blank=True,null=True)
    # socials
    fb_link = models.URLField()
    ig_link = models.URLField()
    linkedIn_link = models.URLField()
    x_link = models.URLField()
    
    def __str__(self):
        return self.name
        # return f"Name - {self.name}"
        
    