from django.db import models

STATUS = (
    ('Available', 'Available'),
    ('Unavailable', 'Unavailable'),
)

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)