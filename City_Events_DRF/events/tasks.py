from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from .models import Event


@shared_task(queue='email')
def send_email_task(subject, message, recipient_email):
    send_mail(
        subject=subject,
        message=message,
        from_email=None,
        recipient_list=[recipient_email],
        fail_silently=True,
    )


@shared_task(queue='email')
def send_new_event_email(event_id):
    event = Event.objects.get(id=event_id)
    users = event.users.model.objects.filter(notify=True, email__gt='')
    subject = f'Новое мероприятие: {event.name}!'
    message = (
        f'Новое мероприятие: {event.name}!\n'
        f'{event.description}\n'
        f'Мероприятие проходит в {event.meeting_time:%d.%m.%Y %H:%M} {event.place}.'
    )

    for user in users:
        send_email_task.delay(subject, message, user.email)


@shared_task(queue='email')
def send_event_reminders():
    now = timezone.now()
    reminder_times = [
        (now + timedelta(days=1), 'завтра'),
        (now + timedelta(hours=6), 'через 6 часов'),
    ]

    for target_time, text_time in reminder_times:
        start = target_time
        end = target_time + timedelta(minutes=5)
        events = Event.objects.filter(meeting_time__gte=start, meeting_time__lt=end)

        for event in events:
            users = event.users.filter(notify=True, email__gt='')
            subject = f'Напоминание о мероприятии: {event.name}'
            message = (
                f'Уведомляем вас, что вы согласились посетить «{event.name}».\n'
                f'{event.description}\n'
                f'Мероприятие проходит {text_time} в '
                f'{event.meeting_time:%d.%m.%Y %H:%M} {event.place}.'
            )

            for user in users:
                send_email_task.delay(subject, message, user.email)
