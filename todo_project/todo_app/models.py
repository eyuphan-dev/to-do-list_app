from django.db import models
from datetime import datetime
# Veri tabanımızı oluşturacağımız tabloları yaptığımız yer burası.
# Create your models here.
# blank=true olursa isteğe bağlı olur boş geçilebilir.
# zaman için datetime kütüphanesini kullandık.
class Todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,blank=True)
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now,blank=True)

# admin bölümünde todoların başlıklarını gösterdik.
    def __str__(self):
        return self.title
