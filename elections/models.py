from django.db import models



# Create your models here.
class Candidate(models.Model):
    BRANCH_CHOICES =[
        ('ME' , 'Mechanical Engineering'),
        ('CSE' , 'Computer Science Engineering'),
        ('ECE' , 'Electronics and Communication Engineering'),
        ('EE' , 'Electrical Engineering'),
        ('EPH' , 'Engineering Physics'),
        ('NON' , 'others or None of the Above')
    ]
    email = models.EmailField(null=True , blank=True)
    name = models.CharField(max_length=32)
    branch = models.CharField(choices=BRANCH_CHOICES , max_length=3)
    enrolno = models.CharField(max_length=8)
    votes = models.IntegerField(default=0)
    image=models.ImageField(null=True, blank=True, upload_to='images/')
    voted_for = models.BooleanField(default=False)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.email}"

