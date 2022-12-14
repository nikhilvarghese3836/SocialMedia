from django.db import models

# Create your models here.
from django.utils.timezone import now

from usermodel.models import User
class Posts(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post_at = models.DateTimeField(blank=True, null=True, default=now)
    text = models.TextField(null=False)
    media_url = models.CharField(max_length=250, blank=True)

    def serialize(self,):
        return {
            'id': self.id,
            'text': self.text,
            'media_url': self.media_url,
            'time':str(self.post_at)
        }
        