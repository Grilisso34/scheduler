from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .forms import *
from .models import *
from .utils import *

# Create your views here.

# menu = ["Хирурги", "Операции"]

class HomePage(DataMixin, ListView):
    model = Surgeon
    template_name = 'surgeons/index.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

# def index(request):
#     names = Surgeon.objects.all()
#     context = {
#         'names': names,
#         'menu': menu,
#         'title': 'Главная страница'
#     }
#     # return render(request, 'surgeons/index.html', {'menu': menu, 'title': 'Главнвя страница'})
#     # return render(request, 'surgeons/index.html', {'names': names, 'menu': menu, 'title': 'Главнвя страница'})
#     return render(request, 'surgeons/index.html', context=context)

class SurgeonsList(DataMixin, ListView):
    model = Surgeon
    context_object_name = 'names'
    template_name = 'surgeons/surgeonslist.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Хирурги')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self) -> QuerySet[Any]:
        return Surgeon.objects.filter(is_published=True)

# def surgeons(request):
#     names = Surgeon.objects.all()
#     context = {
#         'names': names,
#         'menu': menu,
#         'title': 'Главнвя страница'
#     }
#     return render(request, 'surgeons/surgeonslist.html', context=context)

# class SurgInfo(DataMixin, ListView):
#     model = Workschedule
#     context_object_name = 'surginfo'
#     template_name = 'surgeons/surginfo.html'
    
#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         # surginfo = Workschedule.objects.filter(surg_id=self.kwargs.get('surg_id'))
#         duty = Duty.objects.filter(surg_id=self.kwargs.get('surg_id'))
#         receptdays = Receptiondays.objects.filter(surg_id=self.kwargs.get('surg_id'))
#         departures = Scheddepartures.objects.filter(surg_id=self.kwargs.get('surg_id'))
#         name = Surgeon.objects.filter(id=self.kwargs.get('surg_id'))

#         context = super().get_context_data(**kwargs)
#         context['menu'] =  menu
#         context['title'] =  'Информация'
#         context['name'] = str(name[0])
#         # context['surginfo'] = surginfo
#         context['duty'] = duty
#         context['receptdays'] = receptdays
#         context['departures'] = departures
#         return context
    
#     def get_queryset(self) -> QuerySet[Any]:
#         return Workschedule.objects.filter(surg__id=self.kwargs['surg_id'])

class SurgInfo(DataMixin, ListView):
    model = Workschedule
    context_object_name = 'surginfo'
    template_name = 'surgeons/surginfo.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Информация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self) -> QuerySet[Any]:
        return Workschedule.objects.filter(surg__id=self.kwargs['surg_id'])

# def show_surg(request, surg_id):
#     # posts = post.objects.filter(cat_id=cat_id)

#     # if len(posts) == 0:
#     #     raise Http404()

#     # context = {
#     #     'posts': posts,
#     #     'menu': menu,
#     #     'title': 'Categories',
#     #     'cat_selected': cat_id,
#     # }
#     # return render( request, 'blog/index.html', context=context)
#     surginfo = Workschedule.objects.filter(surg_id=surg_id)
#     receptdays = Receptiondays.objects.filter(surg_id=surg_id)
#     name = Surgeon.objects.filter(id=surg_id)
#     departures = Scheddepartures.objects.filter(surg_id=surg_id)
#     duty = Duty.objects.filter(surg_id=surg_id)

#     context = {
#         'surginfo': surginfo,
#         'receptdays': receptdays,
#         'name': name,
#         'departures': departures,
#         'duty': duty,
#         'menu': menu,
#         'title': 'Информация',
#     }
#     return render(request, 'surgeons/surginfo.html', context=context)

class AddSurgeon(LoginRequiredMixin,DataMixin, CreateView):
    form_class = AddSurgeonForm
    template_name = 'surgeons/addsurgeon.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить хирурга')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'surgeons/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self) -> QuerySet[Any]:
        return User.objects.all()
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



# def addsurgeon(request):
#     if request.method == 'POST':
#         form = AddSurgeonForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # try:
#             #     Surgeon.objects.create(**form.cleaned_data)
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка')
#             form.save()
#     else:
#         form = AddSurgeonForm()
#     return render(request, 'surgeons/addsurgeon.html', {'form': form, 'menu': menu, 'title': 'Добавить хирурга'})

# def addsurgeon(request):
#     return render(request, 'surgeons/addsurgeon.html', {'menu': menu, 'title': 'Добавить хирурга'})


# def login(request):
#     return HttpResponse("<h1>Login</h1>")

# def register(request):
#     return HttpResponse("<h1>Registration</h1>")

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'surgeons/login.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    
def logoutuser(request):
    logout(request)
    return redirect('login')

class OperationSurgeionsList(DataMixin, ListView):
    model = Operation
    context_object_name = 'surgeons'
    template_name = 'surgeons/operationsurgeons.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Ответственные хирурги')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self) -> QuerySet[Any]:
        # return OpeartionSchedule.objects.filter(oper__id=self.kwargs['oper_id'])
        return Operation.objects.all()
    

class OperationsList(DataMixin, ListView):
    model = Operation
    template_name = 'surgeons/operationslist.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Операцииgfdgfdgdf')
        return dict(list(context.items()) + list(c_def.items()))
        # return dict(list(c_def.items()))
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     return Operation.objects.filter(surg__id=self.kwargs['surg_id'])

class OperationInfo(DataMixin, ListView):
    model = OpeartionSchedule
    # template_name = 'surgeons/operation.html'
    template_name = 'surgeons/operation.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Операцииf')
        return dict(list(context.items()) + list(c_def.items()))
        # return dict(list(context.items()))
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     return Operation.objects.filter(surg__id=self.kwargs['surg_id'])

# def operations(request):
#     return HttpResponse("<h1>Operations</h1>")

class Operetionnn(DataMixin, ListView):
    model = OpeartionSchedule
    template_name = 'surgeons/operation.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Операция')
        return dict(list(context.items()) + list(c_def.items()))
        # return dict(list(context.items()))

class AddOperation(DataMixin, CreateView):
    form_class = AddOperationForm
    template_name = 'surgeons/addoperation.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Запланировать операцию')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self) -> QuerySet[Any]:
        return OpeartionSchedule.objects.all()