from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from stdimage import StdImageField
# Create your models here.


class Post(models.Model):
    title = models.CharField('Titulo', max_length=255)
    photo = StdImageField('Imagem', upload_to='fotos')
    summary = RichTextField('Resumo')
    content = RichTextUploadingField('Conteudo')
    author = models.CharField('Autor', max_length=50)
    created_at = models.DateField('Criado', auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

