from django.db import models

# Create your models here.
from django.db import models
import uuid
from stdimage.models import StdImageField
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.exceptions import ValidationError
import os

#gerar nome unico para cada arquivo enviado
def get_file_path(_instace, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

def validate_file_extension(value):

    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.ogg', '.wav']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Arquivos de áudio suportados (.MP3, .OGG, .WAV)')

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Post(Base):
    autor = models.ForeignKey(get_user_model(),
                              verbose_name='Autor',
                              on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    sub_titulo = models.CharField('Subtítulo', blank=True, max_length=100)
    post_image = StdImageField(
        'Imagem do Post',
        blank=True,
        upload_to=get_file_path,
        variations={'thumb': {
            'width': 350,
            'height': 200,
            'crop': True
        }})
    audio_post = models.FileField('Áudio do Post',blank=True,
                                  upload_to=get_file_path,
                                  validators=[validate_file_extension])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
