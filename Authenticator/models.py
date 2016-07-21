from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class SeedCompany(models.Model):
    name = models.CharField('Name', max_length=50)
    code = models.CharField('Code', max_length=20)

    def __unicode__(self):
        return '{} {}'.format(self.name, self.code)

    class Meta:
        verbose_name = 'Seed Company'
        verbose_name_plural = 'Seed Companies'

class Product(models.Model):
    name = models.CharField('Name', max_length=40)
    description = models.CharField('Description', max_length=50)
    company = models.ForeignKey(SeedCompany, null=True, blank=False)
    status = models.IntegerField('Status', default=0)
    date_created = models.DateTimeField(default=datetime.now, blank=True, null=True)
    date_of_enquiry = models.DateField('Date of Enquiry')

    def __unicode__(self):
        return '{} {} {}'.format(self.name, self.company, self.description)

    class Meta:
        verbose_name = 'Seed'
        verbose_name_plural = 'Seeds'
