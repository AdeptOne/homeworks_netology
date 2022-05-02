from django.shortcuts import render


from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def books_view_by_date(request, pub_date):
    template = 'books/books_list_by_date.html'
    books_by_date = Book.objects.filter(pub_date=pub_date)

    query_set = Book.objects.values_list('pub_date', flat=True).distinct().order_by('pub_date')

    dates = list(map(str, query_set))
    index_current_date = dates.index(pub_date)

    paginator = {}

    if index_current_date + 1 < len(dates):
        paginator['next_date'] = dates[index_current_date + 1]
    if index_current_date - 1 >= 0:
        paginator['previous_date'] = dates[index_current_date - 1]

    context = {
        'books': books_by_date,
        'paginator': paginator,
    }
    return render(request, template, context)
