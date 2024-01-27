# models.py
from django.db import models
from django.shortcuts import render

class CCTVImage(models.Model):
    image = models.ImageField(upload_to='cctv/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed_image = models.ImageField(upload_to='cctv/processed_images/', blank=True, null=True)
    # Add any additional fields you need for your application

    def save(self, *args, **kwargs):
        # Override the save method to process the image before saving
        self.process_image()
        super().save(*args, **kwargs)

    def process_image(self):
        # Save the processed image
        self.processed_image.save('processed_image.jpg', self.image, save=False)


