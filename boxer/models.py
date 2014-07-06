from django.db import models


class Email(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fro = models.CharField(max_length=255)
    to = models.TextField(blank=True)
    cc = models.TextField(blank=True)
    bcc = models.TextField(blank=True)
    subject = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    html = models.TextField(blank=True)

    def __unicode__(self):
        return "%s > %s" % (self.fro, self.subject)