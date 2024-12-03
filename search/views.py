from django.shortcuts import render
from product.models import Product

def search_results(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objects.filter(name__icontains=query)  # Поиск по части строки в поле name
    return render(request, 'search_results.html', {'results': results, 'query': query})
