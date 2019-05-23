# -*- coding:utf-8 -*-

__author__ = 'bluven'

from rest_framework import serializers
from backend.models import userProfile,aplDatabase,celeryt
from django.contrib.auth import get_user_model
from rest_framework.settings import api_settings


User = get_user_model()

#https://www.jianshu.com/p/17d4c2182ef7
#用户模型获取
#1.获取用户
#User.objects.get/filter  //获取 get获得字典filter获得列表
#User.objects.create(username="xxx")   //创建,注册用户
#user = User.objects.get(xxx)
#user.set_password("xxxxx")

#2.分组
#from django.contrib.auth.models import Group
#Group.objects.create(name = "试用用户组")
#group = Group.objects.get(name = "试用用户组")
#组内所有用户
#users = group.user_set.all()
#用户加入组
#user = User.objects.get(xxx)
#user.groups.add(demo_group)

#注册
#1.表单 示例通过手机注册，暂不包含密码
#class RegisterSerializer(serializers.Serializer):
#    mobile_phone = serializers.INtegerField(allow_null=False)
#    verification_code = serilizers.IntegerField()
#    name = serializers.CharField()
#    company = serializers.CharField()

#2.控制层 整体逻辑
#class Register(APIView):
#    serializer_class = RegisterSerializer
#    
#    def post(self,request,format=None):
#        serializer = RegisterSerializer(data=request.data)
#        if not serializer.is_valid():
#            return render_no_match_v2(serializer.errors)
#
#        mobile_phone - serializer.data["mobile_phone"]
#        ...
#        item = generate_Register_item(mobile_phone, verfication_code, name,company)
#        return render_api_item_v2({"item": item})

#https://www.cnblogs.com/wxiaoyu/p/9588357.html
#from rest_framework_jwt.settings import api_settings
#serializers.py的create方法中添加 手动签发JWT的方法
#jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#生成载荷：包含了user_id,username,email
#payload = jwt_payload_handler(user)
#jwt_token的
#token = jwt_encode_handler(payload)
#将token添加到user: python是面向对象的高级动态编程语言
#user.token = token
#return user



class userProfileSerializer(serializers.ModelSerializer):
    #permissioncode = serializers.CharField(required=True,max_length=40)
    class Meta:
        #model = userProfile
        model = User
        fields = "__all__"
        #fields = ("username","permissioncode")
    
class aplDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = aplDatabase
        fields = "__all__"

class createUserSerializer(serializers.ModelSerializer):
    '''
    用户注册序列化
    '''
    password2 = serializers.CharField(label = '确认密码', write_only = True)
    token = serializers.CharField(label = 'JWT token', read_only = True)
#    mobile = serializers.CharField(label='手机号', write_only = True)    

    class Meta:
        model = User
        fields = ('username','password','password2','token')
        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名',
                }
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }

#    def validate_mobile(self,value):
#        '''验证手机号'''
#        if not re.match(r'^1[3-9]\d{9}$', value):
#            raise serializers.ValidationError('手机号格式错误')
#        return value

    def validate(self,attrs):
        # 判断两次密码
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('输入的两次密码不一致')
        return attrs


    def create(self, validated_data):
        '''重写保存方法,增加密码加密'''

        # 移除数据库模型类中不需要的属性
        # 删除字典数据的两种方法
        # del 字典[key] 删除指定键值对,key不存在不会报错
        # 字典.pop(key) 删除指定键值对,key不存在会报错
        del validated_data['password2']
#        del validated_data['mobile']
        
        # user = User.objects.create(username = xxx, password = xxxx, mobile = xxxx)
        user = User.objects.create(**validated_data)
        
        # 将密码加密,然后保存
        user.set_password(validated_data['password'])
        user.save()

        # 签发JWT Token
        # 报错:AttributeError: Invalid API setting: 'JWT_PAYLOAD_HANDLER'，查看模块位置/python3De/lib/site-packages/rest_framework_jwt/settings.py
        #jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        #jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        # 解决上述签发错误,直接导入jwt_payload_handler,jwt_encode_handler模块
        from rest_framework_jwt.utils import jwt_payload_handler
        from rest_framework_jwt.utils import jwt_encode_handler 
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        # 设置token
        user.token = token

        return user

class celerytSerializer(serializers.ModelSerializer):
    #permissioncode = serializers.CharField(required=True,max_length=40)
    class Meta:
        #model = userProfile
        model = celeryt 
        fields = "__all__"
        #fields = ("username","permissioncode")
