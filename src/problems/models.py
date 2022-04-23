from django.db import models
from django.utils import timezone


class ReportProblem(models.Model):
    user_id = models.IntegerField()
    problem_description = models.CharField(max_length=300)
    serial_number = models.CharField(max_length=64)
    status_indicator_options = [
        ("On", "On"),
        ("Off", "Off"),
        ("Blinking", "Blinking")
    ]
    status_indicator1 = models.CharField(max_length=10, choices=status_indicator_options)
    status_indicator2 = models.CharField(max_length=10, choices=status_indicator_options)
    status_indicator3 = models.CharField(max_length=10, choices=status_indicator_options)

    response_status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
