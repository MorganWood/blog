# 进行users 子应用的视图路由
from django.urls import path
from users.views import RegisterView


urlpatterns = [
    # path的第一个参数是路由
    # path的第二个参数是视图函数名
    path('register/', RegisterView.as_view(), name='register')
]