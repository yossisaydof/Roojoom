from django.shortcuts import render

from server import get_response_status
from .forms import ProblemForm


def home(request):
    return render(request, 'problems/home.html')


def report(request):
    if request.method == 'POST':
        filled_form = ProblemForm(request.POST)
        if filled_form.is_valid():
            form_data = filled_form.cleaned_data
            response_status = get_response_status(form_data)

            # Update response status in DB
            new_form = filled_form.save(commit=False)
            new_form.response_status = response_status
            new_form.save()

            return render(request, 'problems/response.html', {'response_status': response_status})

        filled_form = ProblemForm()
        response_status = 'Report problem has failed. Try again.'
        return render(request, 'problems/report.html', {'problem_form': filled_form, 'response_status': response_status})

    else:
        form = ProblemForm()
        return render(request, 'problems/report.html', {'problem_form': form})
