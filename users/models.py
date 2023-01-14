from django.db import models
from elections.models import Candidate
# Create your models here.
from .manager import UserManager
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    BRANCH_CHOICES =[
        ('ME' , 'Mechanical Engineering'),
        ('CSE' , 'Computer Science Engineering'),
        ('ECE' , 'Electronics and Communication Engineering'),
        ('EE' , 'Electrical Engineering'),
        ('EPH' , 'Engineering Physics'),
        ('NON' , 'others or None of the Above')
    ]
    username = None
    branch = models.CharField(max_length=3,null=True , blank=True , choices=BRANCH_CHOICES)
    name  = models.CharField(max_length=32)
    enrolno = models.CharField(max_length=8  , blank=True)
    email = models.EmailField(unique = True, )

    vote_1_bool = models.BooleanField(default=False)
    vote_2_bool = models.BooleanField(default=False)
    vote_3_bool = models.BooleanField(default=False)
    
    vote_1 = models.ForeignKey(Candidate ,null=True , blank=True, on_delete=models.CASCADE , related_name="candidate1" )
    vote_2 = models.ForeignKey(Candidate ,null=True , blank=True, on_delete=models.CASCADE , related_name="candidate2" )
    vote_3 = models.ForeignKey(Candidate ,null=True , blank=True, on_delete=models.CASCADE , related_name="candidate3")

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return f"{self.email}"



