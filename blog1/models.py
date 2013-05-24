from django.db import models

class Blog1(models.Model):
    publication_date = models.DateTimeField()
    publication_text = models.CharField(max_length=140)

    def __unicode__(self):
        return str(self.publication_date) + '\n' + self.publication_text

    class Meta:
        ordering = ["-publication_date"]     


