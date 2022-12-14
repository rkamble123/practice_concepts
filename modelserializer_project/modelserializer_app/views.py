from django.shortcuts import render
from django.views import View
from .models import UserModel
from .serializers import user_api
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(csrf_exempt,name='dispatch')
class api(View):

    def get(self,request):
        user = UserModel.objects.all()
        print(user)
        serialized_data = user_api(user,many=True)
        return JsonResponse(serialized_data.data,safe=False)
        
    
    def post(self,request):
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer = user_api(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({"Data Created"})
        return HttpResponse({'Something Went Wrong'})


    