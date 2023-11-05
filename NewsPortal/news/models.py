from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.core.cache import cache


class Author(models.Model):
    """ Модель, содержащая объекты всех авторов. """
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        """ Обновляет рейтинг текущего автора.

        Состоит из следующего:
        1. суммарный рейтинг каждой статьи автора умножается на 3;
        2. суммарный рейтинг всех комментариев автора;
        3. суммарный рейтинг всех комментариев к статьям автора.

        """
        user_post_rating = self.post_set.aggregate(Sum('post_rating'))['post_rating__sum']
        user_comment_rating = self.author_user.comment_set.aggregate(Sum('comment_rating'))['comment_rating__sum']
        user_post_comment_rating = 0
        for post in self.post_set.all():
            user_post_comment_rating += post.comment_set.aggregate(Sum('comment_rating'))['comment_rating__sum']
        self.author_rating = 3 * user_post_rating + user_comment_rating + user_post_comment_rating
        self.save()

    def __str__(self):
        return str(self.author_user)


class Category(models.Model):
    """ Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.). """
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    """ Статьи и новости, которые создают пользователи. """
    news = 'NW'
    article = 'AR'
    POST_TYPES_LIST = [
        (news, 'новость'),
        (article, 'статья')
    ]
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POST_TYPES_LIST, default=article)
    post_create_date = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    post_header = models.CharField(max_length=128)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        """ Метод увеличивает рейтинг на единицу """
        self.post_rating += 1
        self.save()

    def dislike(self):
        """ Метод уменьшает рейтинг на единицу """
        self.post_rating -= 1
        self.save()

    def preview(self):
        """ Возвращает начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце """
        return f'{self.post_text[:124]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}') # затем удаляем его из кэша, чтобы сбросить его


class PostCategory(models.Model):
    """ Промежуточная модель для связи «многие ко многим» """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    """ Комментарии к новостям/статьям. """
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_create_date = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        """ Метод увеличивает рейтинг на единицу """
        self.comment_rating += 1
        self.save()

    def dislike(self):
        """ Метод уменьшает рейтинг на единицу """
        self.comment_rating -= 1
        self.save()

class Subscriber(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )


