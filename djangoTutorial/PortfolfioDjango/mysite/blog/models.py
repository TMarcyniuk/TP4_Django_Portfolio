from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title

