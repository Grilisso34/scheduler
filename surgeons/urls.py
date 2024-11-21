from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('surgeons/', SurgeonsList.as_view(), name='surgeons'),
    path('surgeons/<int:surg_id>/', SurgInfo.as_view(), name='surgeon'),
    path('addsurgeon/', AddSurgeon.as_view(), name='add_surgeon'),
    path('operationsurgeons/', OperationSurgeionsList.as_view(), name='operationsurgeons'),
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('logout/', logoutuser, name='logout'),
    # path('operations/', OperationsList.as_view(), name='operations'),
    # path('operations/', operations ,name='operations'),
    # path('operations/<int:oper_id>/', OperationInfo.as_view(), name='operations'),
    path('operations/<int:oper_id>/', OperationsList.as_view(), name='operations'),
    path('operation/<int:oper_id>/', OperationInfo.as_view(), name='operationnn'),
    path('addoperation/', AddOperation.as_view(), name='add_operation'),

    # path('test/', test, name='test'),
    # path('addpage/', add_page, name='add_page'),
    # path('contact/', contact, name='contact'),
    # path('login/', login, name='login'),
    # path('post/<int:post_id>/', show_post, name='post'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    # path('category/<int:cat_id>/', show_category, name='category'),
]
