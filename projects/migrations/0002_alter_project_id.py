# Generated by Django 4.2.2 on 2024-01-25 17:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2a091486-6c55-419f-9245-7be708e99417'), editable=False, primary_key=True, serialize=False),
        ),
    ]
