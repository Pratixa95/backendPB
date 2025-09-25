from django.db import models
from django.utils import timezone

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField()
    mail = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='user_logo/', blank=True, null=True)
    skills = models.TextField(help_text="Comma separated skills", default="")
    tech_stack = models.TextField(help_text="Comma separated technologies", default="")
    project_desc = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    project_img = models.ImageField(upload_to="portfolio/project/", blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

# NEW model for multiple gallery images
class GalleryImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return f"Image for {self.portfolio.name}"


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"