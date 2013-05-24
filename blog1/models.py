from django.db import models

class Publication(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=140)

    def __unicode__(self):
        return str(self.date) + '\n' + self.text

    class Meta:
        ordering = ["-date"]


