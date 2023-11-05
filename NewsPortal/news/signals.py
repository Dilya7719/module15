from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from .models import Subscriber, PostCategory
from .tasks import send_notifications


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.post_category.all()
        subscribers: list[str] = []
        for cat in categories:
            subscribers += Subscriber.objects.filter(category=cat)

        subscribers = [s.user.email for s in subscribers]

        send_notifications.delay(instance.preview(), instance.pk, instance.post_header, subscribers)




