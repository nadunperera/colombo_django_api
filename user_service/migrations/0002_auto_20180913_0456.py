# Generated by Django 2.1.1 on 2018-09-13 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lead_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_service.LeadSource'),
        ),
    ]