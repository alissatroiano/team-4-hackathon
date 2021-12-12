# Generated by Django 4.0 on 2021-12-12 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0002_alter_date_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='calendar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='dates.calendar'),
        ),
    ]
