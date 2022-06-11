#views.py

from django.http import JsonResponse
from django.views import View
from logs.models import Log
from datetime import datetime

class LogView(View):
    def get(self, request):
        ip_address = request.META['REMOTE_ADDR']
        access_time = datetime.now()

        if not Log.objects.filter(ip=ip_address).exists():

        Log.objects.create(
            ip_address = ip_address,
            access_time = access_time
        )

        logs = Log.objects.all()

        log_list = [{
            'ip_address' : log.ip_address,
            'access_time' : log.access_time
        }for log in logs]

        return JsonResponse({'result':log_list}, status=200)