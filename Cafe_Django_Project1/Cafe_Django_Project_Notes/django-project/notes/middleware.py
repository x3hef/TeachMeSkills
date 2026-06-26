from pathlib import Path

from django.conf import settings
from django.utils import timezone


class UserActivityLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_file = Path(settings.BASE_DIR) / 'usersActivity.log'

    def __call__(self, request):
        username = request.user.username if request.user.is_authenticated else 'anonymous'
        current_time = timezone.localtime().strftime('%m.%d.%Y %H:%M')
        url = request.get_full_path()

        with self.log_file.open('a', encoding='utf-8') as file:
            file.write(f'{current_time} | {username} | URL={url}\n')

        return self.get_response(request)
