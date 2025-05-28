from django.db import models

class UploadedPDF(models.Model):
    file = models.FileField(upload_to='pdf/')