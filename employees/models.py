from django.db import models
from django.contrib.auth.models import User
# готовая модель, которую мы поменяем
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
# чтобы отслеживать из бд сигналы (прошла ли регистрация успешно (для себя))
from django.dispatch import receiver
# чтобы подключиться к миддлвер


class JobApplication(User):
    LEVEL = (
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    phone_number = models.CharField(max_length=14, default='+996', db_index=True, null=True)
    age = models.PositiveIntegerField(default=18,
                                      validators=[
                                          MaxValueValidator(60),
                                          MinValueValidator(18),
                                      ], db_index=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, db_index=True, null=True)
    level = models.CharField(max_length=10, choices=LEVEL, db_index=True, null=True)
    salary = models.IntegerField(default=0, db_index=True, null=True)


# пометка в консоли, чтобы мы видели операцию и как все проходит
@receiver(post_save, sender=JobApplication)
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