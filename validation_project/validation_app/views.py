from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from .models import stu_model
from .serializers import stu_serializer
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.serializers import Serializer


# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class stu_api(View):

    def get(self,request,*args,**xargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id=parsed_data.get('id')
        stu = stu_model.objects.get(id=id)
        serialized_data = stu_serializer(stu)
        return JsonResponse(serialized_data.data,safe=False)


    def post(self,request,*args,**xargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        serialized_data = stu_serializer(data = parsed_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({"msg":"Data Created"})
        error = JSONRenderer().render(serialized_data.errors)
        return HttpResponse(error,content_type = 'application/json')


