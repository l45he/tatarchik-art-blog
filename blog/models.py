from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField('Название', max_length=100, help_text='Название поста')
    text = models.TextField('Текст поста')
    image = models.ImageField('Изображение', upload_to='images')
    publication_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    # автоматическое подставление динамического параметра в url-адрес
    # def get_absolute_url(self):
    #     return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'
