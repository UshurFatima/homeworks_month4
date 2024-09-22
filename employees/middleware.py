from django.utils.deprecation import MiddlewareMixin
# помогает распределить роли
from django.http import HttpResponseBadRequest
# проверка удачно или нет отправлен запрос


class SalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # указываем как, через какой путь будет определять зарплату(регистрация)
        # как только регистрируемся, должен срабатывать миддлвер, чтоб определить роль
        if request.path == '/register/' and request.method == 'POST':
            level = str(request.POST.get('level'))
            if level == 'Junior':
                request.salary = 500
            elif level == 'Middle':
                request.salary = 1000
            elif level == 'Senior':
                request.salary = 3000
            else:
                return HttpResponseBadRequest('Такого уровня нет!')

        elif request.path == '/register/' and request.method == 'GET':
            # устанавливает значение атрибута указанного объекта по его имени
            setattr(request, 'salary', 'Зарплата не определена')
