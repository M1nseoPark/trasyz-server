from django.http import JsonResponse
from django.shortcuts import render
from .models import Parkinglot

def index(request):
    parkinglots = Parkinglot.objects.all()

    return render(
        request,
        'manager/index.html',
        {
            'parkinglots': parkinglots,
        }
    )

def get_post(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        mid = request.GET['mid']
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']

        parkinglot = {
            'pid': pid,
            'mid': mid,
            'latitude': latitude,
            'longitude': longitude,
        }

        return render(request, 'manager/rent.html', parkinglot)


# class ParkinglotView(View):
#     def get(self, request, *args, **kwargs):
#         # GET 요청을 통해 들어온 HTTP request 받음
#         # -> 쿼리 파라미터 pid키에 해당하는 값을 get()을 통해 얻겠다는 것
#         parkinglot_id = request.GET.get('pid', None)
#         pm_id = request.GET.get('mid', None)
#         latitude = request.GET.get('latitude', None)
#         longitude = request.GET.get('longitude', None)
#
#         return render(
#             request,
#             'manager/index.html',
#             parkinglot_id,
#         )

        # # parkinglot_id를 통해 Parkinglot에 접근하여 일치하는 주차장 아이디를 갖는 객체를 호출함
        # parkinglot = Parkinglot.objects.get(id=parkinglot_id)
        #
        # # 위의 객체를 parkinglot_information에 객체 형태로 담아 전송
        # parkinglot_information = {
        #     "parkinglot_id": parkinglot.id,
        # }
        #
        # # HTTP GET 요청에 대한 응답으로 JSON 형식의 데이터를 제공하고, 상태 코드 200을 반환함
        # return JsonResponse({"message": parkinglot_information}, status=200)

