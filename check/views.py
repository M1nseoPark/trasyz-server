import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from check.models import Parkinglot


# Create your views here.
class IndexView(View):
    def get(self, request):
        parkinglots = Parkinglot.objects.all()

        return render(
            request,
            'check/index.html',
            {
                'parkinglots': parkinglots,
            }
        )
    def put(self, request):
        request = json.loads(request.body)
        pid = request['pid']
        kickboard = request['kickboard']
        parkinglots = get_object_or_404(Parkinglot, pk=pid)
        parkinglots.kickboard += kickboard
        parkinglots.save()
        return HttpResponse(status=200)