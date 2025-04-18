# Generated by Django 5.1.4 on 2025-01-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartwatch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthdata',
            old_name='sleep_duration',
            new_name='calories_burned',
        ),
        migrations.RenameField(
            model_name='healthdata',
            old_name='heart_rate',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='healthdata',
            name='steps',
        ),
        migrations.AddField(
            model_name='healthdata',
            name='age',
            field=models.IntegerField(default=25),
        ),
        migrations.AddField(
            model_name='healthdata',
            name='exercise',
            field=models.CharField(choices=[('walking', 'Walking'), ('running', 'Running'), ('cycling', 'Cycling'), ('swimming', 'Swimming'), ('yoga', 'Yoga')], default='walking', max_length=20),
        ),
        migrations.AddField(
            model_name='healthdata',
            name='weight',
            field=models.FloatField(default=70),
        ),
    ]
