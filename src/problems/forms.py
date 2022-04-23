from django import forms
from .models import ReportProblem


class ProblemForm(forms.ModelForm):
    class Meta:
        model = ReportProblem
        fields = [
            'user_id',
            'problem_description',
            'serial_number',
            'status_indicator1',
            'status_indicator2',
            'status_indicator3'
        ]
        labels = {
            'user_id': 'User ID',
            'problem_description': 'Problem description',
            'serial_number': 'Serial number',
            'status_indicator1': 'Status Indicator Light 1',
            'status_indicator2': 'Status Indicator Light 2',
            'status_indicator3': 'Status Indicator Light 3'
        }
