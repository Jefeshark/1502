from django.db import models

# Create your models here.
# https://azinkin.ru/orm.html

class Category(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='контент',
        blank=True,
    )
    picture = models.ImageField(
        verbose_name='картинка',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=False,
    )
    category = models.ForeignKey(
        verbose_name='категория',
        to='Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'публикации'
        unique_together = ('category', 'slug')

class Comment(models.Model):
    post = models.ForeignKey(
        on_delete=models.CASCADE,
        to='Post',
        verbose_name="Публикации",
    )
    name = models.CharField(
        verbose_name="Имя/Фамилия",
        max_length=120,
    )

    content = models.TextField(
        verbose_name="Комментарии",
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now=True,
    )

    parent_comment = models.ForeignKey(
        verbose_name="Родительский комментарий",
        to='self',
        on_delete=models.CASCADE,
        null=True,
    )

    def str(self):
        return f"Комментарий от {self.name} к {self.post.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Like (models.Model):
    post = models.ForeignKey(
        verbose_name="Публикации",
        to='Post',
        on_delete=models.CASCADE,
)
    reaction = models.IntegerField(
        choices=[(1, 'Like'),
                (-1, 'Dislike')],
        verbose_name="Реакция",
    )
    data = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now=True,
)

    def str(self):
        return f" {self.post.title}"

    class Meta:
        verbose_name = "Реакция"
        verbose_name_plural = "Реакции"


class Donat(models.Model):
    png = models.ImageField(
        verbose_name="Картинка",
)
    name = models.CharField(
        verbose_name="Название",
        max_length=120,
)
    url = models.URLField(
        verbose_name="Ссылка",
)

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Донат"
        verbose_name_plural = "Донаты"