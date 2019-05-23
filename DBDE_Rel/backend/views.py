from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from .tasks import run_test 

from .models import userProfile,aplDatabase,celeryt
from .serializer import userProfileSerializer,aplDatabaseSerializer,createUserSerializer,celerytSerializer
from .tasks import celeryTouch

import os
import datetime
from .logger_init import mlog
# Create your views here.

#示例 购物车需要token认证才能查看
#
#class ShoppingCartViewset(viewsets.ModelViewSet):
#    '''
#    购物车功能
#    list:
#        获取购物车详情
#    create:
#        加入购物车
#    delete:
#        删除购物记录
#    '''
#    permission_class = (IsAuthenticated, IsOwnerOrReadOnly)
#    #标记需要进行jwt验证
#    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
#    serializer_class = ShopCartSerializer
#    lookup_field = "goods_id"

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class userProfileViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    用户表
    '''
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    pagination_class = StandardResultsSetPagination

#@permission_classes((IsAuthenticated, ))
class aplDatabaseViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    数据库申请
    '''
    queryset = aplDatabase.objects.all()
    serializer_class = aplDatabaseSerializer
    pagination_class = StandardResultsSetPagination

class registerUserViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    用户申请
    '''
    queryset = userProfile.objects.all()
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    permission_classes = (AllowAny,)
    serializer_class = createUserSerializer 
    
    

def tasks(requests):
    print('setup1')
    result = run_test
    if result:
        print('run_test task success!')


class celerytViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    '''
    celery测试任务
    '''
    queryset =  celeryt.objects.all()
    serializer = celerytSerializer
    
    '''
    重写 create/post方法
    '''
    def create(self, request, *args, **kwargs):
        now_time = datetime.datetime.now()
        nowTime = now_time.strftime('%Y-%m-%d %H:%M:%S')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            mlog().log_info('Start  test celery task at %s' % nowTime)
            celeryTouch
        
        self.perform_create(serializer) 
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
 
    '''
    mixin中create中其他内容 
    def perform_create(self, serializer):
        serializer.save()   #post需要保存serializer      
  
    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):   
            return {}
    '''
