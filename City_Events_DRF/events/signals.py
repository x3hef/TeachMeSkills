from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event
from .tasks import send_new_event_email


@receiver(post_save, sender=Event)
def event_saved(sender, instance, created, **kwargs):
    # Event list is cached, so after changes we remove old cached data.
    cache.delete('future_events')

    if created:
        try:
            send_new_event_email.delay(instance.id)
        except Exception:
            # If Redis/Celery is not running during local checking, the project should not crash.
            pass
