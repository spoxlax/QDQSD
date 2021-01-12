from django.db import models
# from account.models import Account
from django.conf import settings


# Create your models here.
class Priority(models.Model):
    COLOR = (
        ('LOW', 'white'),
        ('MEDIUM', 'blue'),
        ('NORMAL', 'green'),
        ('HIGH', 'orange'),
        ('VERY-HIGH', 'RED'),
    )
    NAME = (
        ('white', 'LOW'),
        ('blue', 'MEDIUM'),
        ('green', 'NORMAL'),
        ('orange', 'HIGH'),
        ('RED', 'VERY-HIGH'),
    )
    name = models.CharField(max_length=10, choices=NAME)
    color = models.CharField(max_length=10, null=True, choices=COLOR)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField(max_length=600)
    html = models.TextField()
    attachement = models.FileField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    completed_at = models.DateTimeField()

    def __str__(self):
        return self.subject + ' ' + self.status.name + ' ' + self.priority.name

    # key = models.CharField()
    # Titile = models.CharField()
    # sender = models.EmailField
    # receiver = models.EmailField()
    # description = models.CharField()
    # attachement = models.FileField()
    # # contact = models.EmailField()
    # groupe = models.IntegerField()
    # source = models.CharField()
    # created_at = models.DateTimeField()
    # status = models.CharField()
    # type = models.CharField()
    # company = models.IntegerField()
    # priority = models.CharField()
    # closed_at = models.DateTimeField()
    # resolved_by = models.IntegerField()
