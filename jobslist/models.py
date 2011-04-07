from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    url  = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(Company)
    title   = models.CharField(max_length=24)
    desc    = models.CharField(max_length=512)
    salary  = models.CharField(max_length=12)
    def __unicode__(self):
        return self.title
