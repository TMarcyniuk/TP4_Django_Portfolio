from django.db import models
from django.conf import settings
from django.utils import timezone
import os

def validate_file_extension(value):
    """Validar que el archivo sea imagen o video"""
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mov', '.avi', '.webm', '.mkv']
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in valid_extensions:
        from django.core.exceptions import ValidationError
        raise ValidationError('Formato de archivo no soportado. Solo se permiten imágenes (jpg, png, gif) y videos (mp4, mov, avi, webm, mkv).')

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    título = models.CharField(max_length=200)
    texto = models.TextField()
    archivo = models.FileField(blank=True, upload_to='posts/', validators=[validate_file_extension])

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self): 
        return self.título
    
    def publish(self):
        self.published_date = timezone.now()

    def is_image(self):
        """Verificar si el archivo es una imagen"""
        if not self.archivo:
            return False
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        ext = os.path.splitext(self.archivo.name)[1].lower()
        return ext in image_extensions
    
    def is_video(self):
        """Verificar si el archivo es un video"""
        if not self.archivo:
            return False
        video_extensions = ['.mp4', '.mov', '.avi', '.webm', '.mkv']
        ext = os.path.splitext(self.archivo.name)[1].lower()
        return ext in video_extensions

    def recent_comments(self):
        """Devuelve todos los comentarios ordenados del más reciente al más antiguo"""
        return self.comments.all().order_by('-created_date')


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    autor = models.CharField(max_length=20)
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.texto