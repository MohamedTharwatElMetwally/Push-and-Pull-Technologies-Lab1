import os
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.conf import settings

class FilePollingView(View):
    def get(self, request, *args, **kwargs):
        client_time = int(request.GET.get('lastmod', 0))
        file_path = os.path.join(settings.BASE_DIR, 'mycv.txt')
        file_time = int(os.path.getmtime(file_path))

        while client_time >= file_time:
            time.sleep(1)
            file_time = int(os.path.getmtime(file_path))

        with open(file_path, 'r') as file:
            file_content = file.read()

        message = {
            'data': file_content,
            'filetime': file_time,
        }
        return JsonResponse(message)

# Disable CSRF protection for this view
@method_decorator(csrf_exempt, name='dispatch')
class FilePollingViewExempt(FilePollingView):
    pass
