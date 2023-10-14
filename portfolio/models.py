from django.db import models
from django.urls import reverse
from transliterate import slugify


# Create your models here.
class Artworks(models.Model):
    title = models.CharField('Название проекта', max_length=100)
    slug = models.SlugField('Уникальное название', unique=True, blank=True)
    main_image = models.ImageField('Основное изображение', upload_to='images')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Artworks, self).save(*args, **kwargs)

    #отображение картинок в админ панели
    # def image_display(self):
    #     if not self.main_image:
    #         return f'/media/images/}'
    #     return self.avatar.url

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'Мои проекты'

    def get_absolute_url(self):
        return reverse('one_artwork', kwargs={'slug': self.slug})


class Images(models.Model):
    title = models.CharField('Название работы', max_length=100, default='Работа без названия')
    image = models.ImageField('Изображение работы')
    artwork = models.ForeignKey('Artworks', on_delete=models.CASCADE, verbose_name='Привязка к проекту')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'работу'
        verbose_name_plural = 'Работы'