# Generated by Django 2.1.1 on 2018-09-13 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_service', '0002_auto_20180913_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lead_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user_service.LeadSource'),
        ),
    ]