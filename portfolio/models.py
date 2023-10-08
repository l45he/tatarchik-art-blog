from django.db import models

# Create your models here.
class Artworks(models.Model):
    title = models.CharField('Название проекта', max_length=100)
    main_image = models.ImageField('Основное изображение', upload_to='images')

    def __str__(self):
        return self.title

    #отображение картинок в админ панели
    # def image_display(self):
    #     if not self.main_image:
    #         return f'/media/images/}'
    #     return self.avatar.url

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'Мои проекты'


class Images(models.Model):
    title = models.CharField('Название работы', max_length=100, default='Работа без названия')
    image = models.ImageField('Изображение работы')
    artwork = models.ForeignKey('Artworks', on_delete=models.CASCADE, verbose_name='Привязка к проекту')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'работу'
        verbose_name_plural = 'Работы'