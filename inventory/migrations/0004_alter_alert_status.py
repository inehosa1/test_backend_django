# Generated by Django 5.0.3 on 2024-03-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_alert_is_sent_alert_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('expired', 'Expired'), ('pending', 'Pending')], default='pending', max_length=10),
        ),
    ]
