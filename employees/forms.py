from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

LEVEL = (
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    )
GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )


class ApplicationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    level = forms.ChoiceField(choices=LEVEL, required=True)

    # выписываем, что мы хотим видеть в форме
    class Meta:
        model = models.JobApplication
        fields = (
            'first_name',
            'last_name',
            'age',
            'gender',
            'username',
            'email',
            'phone_number',
            'level',
            'password1',
            'password2'
        )

    # сохраняем данные из формы
    def save(self, commit=True):
        employee = super(ApplicationForm, self).save(commit=False)
        employee.email = self.cleaned_data['email']
        if commit:
            employee.save()
        return employee


@receiver(post_save, sender=models.JobApplication)
def set_salary(sender, instance, created, **kwargs):
    if created:
        print('Сигнал обработан. Пользователь создан')

        level = instance.level
        if level == 'Junior':
            instance.salary = 500
        elif level == 'Middle':
            instance.salary = 1000
        elif level == 'Senior':
            instance.salary = 3000
        else:
            instance.salary = 0
        instance.save()