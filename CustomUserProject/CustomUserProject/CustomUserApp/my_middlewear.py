from django.http import HttpResponse
import socket
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

class Nimap_middlewear:
    def __init__(self,get_response):
        self.get_response = get_response
        print('Custom Middlewear')

    # def __call__(self,request):
    #     print('This is before view')
    #     response = self.get_response(request)
    #     print('This is after view')
    #     return response


    # def process_request(request):
    #     print('In the process request ')
    #     request_path = request.get_full_path()
    #     print(request_path)

    #     # print(request.get_host())
    #     # hosted_by_nimap = request.gethostname()
    #     # print(hosted_by_nimap)
    #     # if hosted_by_nimap not in ['127.0.0.1:8000','192.168.0.1']:
    #     #     self.proess_exception()
    #     return request

    # def __init__(self, get_response):
    #     self.get_response = get_response
    #     print(self.get_response)

    # def process_request(self, request):
    #     host = request.get_host()
    #     print(host)
    #     # return None

    # def __call__(self,request):
    #     print('This is before view')
    #     return request


    def process_request(self, request):

        print('In the process request ')
        request_path = request.get_full_path()
        print(request_path)

        # # print(request.get_host())
        # # hosted_by_nimap = request.gethostname()
        # # print(hosted_by_nimap)
        # # if hosted_by_nimap not in ['127.0.0.1:8000','192.168.0.1']:
        # #     self.proess_exception()
        # return request


        host = request.get_host()
        print(host)
        if host not in ['127.0.0.1:8000','192.168.0.1']:
            self.process_exception(request)
        # print (exception.__class__.__name__)
        # print (exception.message)
        return request

    def __call__(self,request):
        print('This is before view')
        # host = request.get_host()
        # print(host)
        # if host not in ['127.0.0.1:8000','192.168.0.1']:
        #     self.process_exception(request)
        # request_path = request.get_full_path()
        # print(request_path)
        # response = self.get_response(request)
        # host_name = socket.gethostname()
        # print(host_name)
        response = self.get_response(request)
        print('This is after view')
        return response

    
class NewMiddlewear:
    def __init__(self,get_response):
        self.get_response = get_response
        print('Custom Middlewear')

    def process_request(self, request):
        print('In the process request ')
        request_path = request.get_full_path()
        print(request_path)
        host_name = request.get_host()
        print('get_host : ',request.get_host())
        print('gethostname : ',socket.gethostname())
        if host_name not in ['127.0.0.1:8000','192.168.0.1']:
            return self.process_exception(request,exception=ValueError())
        return request


    def __call__(self,request):
        print('This is before view')
        request=self.process_request(request)
        response = self.get_response(request)
        print('This is after view')
        return response


    def process_exception(self,request,exception):
        print(type(request))
        return request