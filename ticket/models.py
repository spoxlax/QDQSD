from django.db import models


# Create your models here.
class Ticket(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    html = models.TextField()
    attachement = models.FileField()
    status_id = models.CharField(max_length=200)
    priority_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    agent_id = models.CharField(max_length=200)
    category_id = models.CharField(max_length=200)
    groupe_id = models.CharField(max_length=200)
    company_id = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    completed_at = models.CharField(max_length=200)

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
