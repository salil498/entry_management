# Generated by Django 2.0.6 on 2019-11-27 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('em', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='host_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='em.HostDetails'),
        ),
    ]
