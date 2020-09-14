from django.shortcuts import render
from search.documents import ArsenalDocument

# Create your views here.
def search(request):

    q = request.GET.get('q')

    if q:
        arsenals = ArsenalDocument.search().query("match", title=q)
    else:
        arsenals = ''

    return render(request, 'search/search.html', {'arsenals': arsenals})