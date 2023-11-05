from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from news.models import Post, Subscriber


@shared_task
def mailing():
    date_now = timezone.now()
    date_now_week_ago = date_now - timedelta(days=30)
    posts = Post.objects.filter(post_create_date__gte=date_now_week_ago)
    categories_id = set(posts.values_list('post_category', flat=True))
    subscribers = []
    for cat in categories_id:
        subscribers += Subscriber.objects.filter(category=cat)
    subscribers = set([s.user.email for s in subscribers])

    html_content = render_to_string(
        'posts_compilation_email.html',
        {
            'link': settings.SITE_URL,
            'posts': posts
        }
    )

    msg = EmailMultiAlternatives(
        subject='Новые статьи за прошедшую неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

