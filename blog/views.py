from django.shortcuts import render
from .models import User
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
# Create your views here.


def login(request):
    if request.method == "GET":
        data = User.objects.all()
        json_data = serializers.serialize('json', data)
        json_data = json.loads(json_data)
        ss = []
        for i in range(len(json_data)):
            ss.append(json_data[i]['fields'])
        ok = {
            'data': ss
        }
        return JsonResponse(ok, safe=False)
