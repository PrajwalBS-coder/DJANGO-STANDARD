# Generated by Django 5.1.6 on 2025-02-21 19:33

import django.core.validators
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'female'), ('O', 'Others')], max_length=1)),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('Dev', 'Developer'), ('PM', 'Project Manager'), ('QA', 'Quality Analyst'), ('UX', 'UI/UX Designer')], max_length=3)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employee',
                'ordering': ['-date_joined'],
            },
        ),
    ]
