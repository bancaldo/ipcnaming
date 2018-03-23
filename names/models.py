# noinspection PyUnresolvedReferences
from django.db import models


class Component(models.Model):
    type_of = models.CharField(max_length=3)
    prefix = models.CharField(max_length=16)
    description = models.CharField(max_length=256)
    pattern = models.CharField(max_length=64)
    arguments = models.CharField(max_length=256)

    def __unicode__(self):
        return "[%s] %s" % (self.type_of, self.prefix)
