from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class Publication(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=140)
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return str(self.date) + '\n' + self.text

    def get_absolute_url(self):
        return reverse('msglist') #, kwargs={'pk': self.pk})

    class Meta:
        ordering = ["-date"]

