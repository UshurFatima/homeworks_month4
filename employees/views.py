# готовая форма для аутентификации
from django.contrib.auth.forms import AuthenticationForm
# чтоб когда мы нажимали войти, данные сохранялись в сессию (на время),
# а когда выйти - удалялись
from django.contrib.auth.views import LoginView, LogoutView
# чтобы данные передавались не через урлы
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy  # для логаута
from . import models, middleware, forms


@method_decorator(cache_page(60*15), name='dispatch')
class RegistrationView(CreateView):
    template_name = 'employees/register.html'
    form_class = forms.ApplicationForm
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        level = form.cleaned_data['level']
        if level == 'Junior':
            self.object.salary = 500
        elif level == 'Middle':
            self.object.salary = 1000
        elif level == 'Senior':
            self.object.salary = 3000
        else:
            self.object.salary = 0
        self.object.save()
        return response


@method_decorator(cache_page(60*15), name='dispatch')
class AuthLoginView(LoginView):
    template_name = 'employees/login.html'
    form_class = AuthenticationForm

    # после авторизации перебросит на список всех
    def get_success_url(self):
        return reverse('employees:employee_list')


@method_decorator(cache_page(60*15), name='dispatch')
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('employees:login')


@method_decorator(cache_page(60*15), name='dispatch')
class EmployeeListView(ListView):
    template_name = 'employees/employee_list.html'
    model = models.JobApplication

    def get_queryset(self):
        return self.model.objects.all()

    # чтоб получать данные о зарплате
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salary'] = getattr(self.request, 'salary', 0)
        return context
