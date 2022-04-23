# Generated by Django 4.0.4 on 2022-04-23 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('problem_description', models.CharField(max_length=300)),
                ('serial_number', models.CharField(max_length=64)),
                ('status_indicator1', models.CharField(choices=[('On', 'On'), ('Off', 'Off'), ('Blinking', 'Blinking')], max_length=10)),
                ('status_indicator2', models.CharField(choices=[('On', 'On'), ('Off', 'Off'), ('Blinking', 'Blinking')], max_length=10)),
                ('status_indicator3', models.CharField(choices=[('On', 'On'), ('Off', 'Off'), ('Blinking', 'Blinking')], max_length=10)),
                ('response_status', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
