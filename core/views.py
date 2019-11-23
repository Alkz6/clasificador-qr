from django.shortcuts import render

# Create your views here.

def main(request, *args, **kargs):
    context = {}
    template_name = 'core/main.html'
    if request.method == 'POST':
        pass
    return render(request, template_name, context)
