from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст публикации'
    )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True,
        help_text='Если установить дату и время '
                  'в будущем — можно делать отложенные '
                  'публикации.'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор публикации',
        help_text='Автор публикации'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True,
        verbose_name="Изображение",
        help_text="Изображение"
    )
    group = models.ForeignKey(
        'Group', on_delete=models.CASCADE, related_name='posts', blank=True,
        null=True, verbose_name='Группы',
        help_text='Группа'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('id', 'author', 'group')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор комментария',
        help_text='Автор комментария')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', blank=True,
        verbose_name='Публикация',
        help_text='Публикация')
    text = models.TextField(verbose_name='Текст комментария',
                            help_text='Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True,
        help_text='Дата комментария')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created',)


class Group(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
        help_text='Заголовок сообщества'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание сообщества'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
                  'разрешены символы латиницы, цифры, '
                  'дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower',
        verbose_name="Подписавшийся пользователь",
        help_text='Подписавшийся пользователь'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        verbose_name='Пользователь, на которого подписались',
        help_text='Пользовтель, на которого подписались'
    )

    class Meta:
        verbose_name = 'подписка',
        verbose_name_plural = 'Подписки'
        ordering = ('id',)

    def __str__(self):
        return f'{self.user} {self.following}'
