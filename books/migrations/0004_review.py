# Generated by Django 5.1.1 on 2024-09-11 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_review', to='books.book')),
            ],
        ),
    ]
