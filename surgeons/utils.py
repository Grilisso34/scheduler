from surgeons.models import *


menu = [
    {'title': "Хирурги", 'url_name': 'surgeons'},
    {'title': "Операции", 'url_name': 'operationsurgeons'},
    # {'title': "Войти", 'url_name': 'login'},
    # {'title': "Регистрация", 'url_name': 'registration'},
    {'title': "Добавить хирурга", 'url_name': 'add_surgeon'},
    {'title': "Запланировать операцию", 'url_name': 'add_operation'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        duty = Duty.objects.filter(surg_id=self.kwargs.get('surg_id'))
        receptdays = Receptiondays.objects.filter(surg_id=self.kwargs.get('surg_id'))
        departures = Scheddepartures.objects.filter(surg_id=self.kwargs.get('surg_id'))
        name = Surgeon.objects.filter(id=self.kwargs.get('surg_id'))

        operation = Operation.objects.filter(surg_id=self.kwargs.get('oper_id'))
        opersched = OpeartionSchedule.objects.filter(oper_id=self.kwargs.get('oper_id'))
        patinfo = PatientInfo.objects.filter(oper_id=self.kwargs.get('oper_id'))

        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        context['menu'] = user_menu
        context['name'] = name
        context['duty'] = duty
        context['receptdays'] = receptdays
        context['departures'] = departures

        context['operation'] = operation
        context['opersched'] = opersched
        context['patinfo'] = patinfo
        return context