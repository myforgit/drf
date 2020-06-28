from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from logines.models import User


@method_decorator(csrf_exempt, name="dispatch")  # 让类视图免除csrf认证
class UserView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        print(user_id)
        if user_id:  # 查询单个
            user_val = User.objects.filter(id=user_id).values("username", "password").first()
            if user_val:
                # 如果查询出对应的用户信息，则将用户的信息返回到前端
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": user_val
                })
        else:
            user_list = User.objects.all().values("username", "password")
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "message": "查询所有用户成功",
                    "results": list(user_list),
                })

        return JsonResponse({
            "status": 500,
            "message": "查询失败",
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        print(username)
        pwd = request.POST.get("password")
        print(pwd)
        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "password": user_obj.password}
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })
class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):

        print(request._request.GET)

        print(request.GET)

        print(request.query_params)

        return Response("DRF GET SUCCESS")

    def post(self, request, *args, **kwargs):
        print(request._request.POST)
        print(request.POST)
        print(request.data)

        return Response("POST GET SUCCESS")