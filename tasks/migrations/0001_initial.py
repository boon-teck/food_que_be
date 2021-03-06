# Generated by Django 3.2.5 on 2021-07-13 09:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name_of_task', models.CharField(max_length=50)),
                ('description_to_buy', models.TextField(max_length=5000)),
                ('cost_of_food', models.IntegerField()),
                ('budget', models.IntegerField()),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
