from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from assignments.models import Canvas, CanvasAssignment
from .forms import FileUploadForm, HTMLInputForm


def dashboard(request):
    canvas = Canvas.objects.first()
    assignments = canvas.get_todo()
    context = {'assignments': assignments}
    return render(request, 'assignments/dashboard.html', context)


def assignment(request, assignment_id):
    try:
        assignment = CanvasAssignment.objects.get(pk=assignment_id)
    except CanvasAssignment.DoesNotExist:
        raise Http404("Assignment does not exist")

    if request.method == 'POST':
        file_form = FileUploadForm(request.POST)

        if file_form.is_valid():
            url = file_form.data['url']
            submission = assignment.canvasfilesubmission_set.first()
            submission.submit(url=url)
            return HttpResponseRedirect('/assignments')

        text_form = HTMLInputForm(request.POST)
        if text_form.is_valid():
            text = text_form.data['text']
            submission = assignment.canvastextsubmission_set.first()
            submission.submit(text)
            return HttpResponseRedirect('/assignments')
    else:
        context = {'assignment': assignment}

        if assignment.canvastextsubmission_set.all():
            context['text_input_form'] = HTMLInputForm()

        if assignment.canvasfilesubmission_set.all():
            context['file_upload_form'] = FileUploadForm()

        if ('file_upload_form' in context) or ('text_input_form' in context):
            context['forms'] = 1

        return render(request, 'assignments/detail.html', context)