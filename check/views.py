import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from check.models import Parkinglot, Run


# Create your views here.
class IndexView(View):
    def get(self, request):
        runs = Run.objects.all()
        parkinglots = Parkinglot.objects.all()

        return render(
            request,
            'check/index.html',
            {
                'runs' : runs,
                'parkinglots': parkinglots,
            }
        )

    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            pm = Run(rid = request['rid'],
                     latitude = request['latitude'],
                     longitude = request['longitude'])
        else:
            pm = Run(rid = request.POST['rid'],
                     latitude = request.POST['latitude'],
                     longitude = request.POST['longitude'])
        pm.save()
        return HttpResponse(status=200)

    def put(self, request):
        request = json.loads(request.body)
        pid = int(request['pid'])
        kickboard = int(request['kickboard'])
        parkinglots = get_object_or_404(Parkinglot, pk=pid)
        parkinglots.kickboard += kickboard
        parkinglots.save()
        return HttpResponse(status=200)