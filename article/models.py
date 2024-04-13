from django.db import models
NULLABLE = {'null': True, 'blank': True}


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=20, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='articles/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    view_count = models.IntegerField(verbose_name='Количество просмотров', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
