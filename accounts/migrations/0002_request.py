# Generated by Django 5.0.2 on 2024-03-12 03:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('two wheeler with gear', 'two wheeler with gear'), ('two wheeler without gear', 'two wheeler without gear')], max_length=50)),
                ('vehicle_no', models.PositiveIntegerField()),
                ('vehicle_name', models.CharField(max_length=40)),
                ('vehicle_model', models.CharField(max_length=40)),
                ('vehicle_brand', models.CharField(max_length=40)),
                ('problem_description', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('cost', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Repairing', 'Repairing'), ('Repairing Done', 'Repairing Done'), ('Released', 'Released')], default='Pending', max_length=50, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_request', to=settings.AUTH_USER_MODEL)),
                ('mechanic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
                'abstract': False,
            },
        ),
    ]
