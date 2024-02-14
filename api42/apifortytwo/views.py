# views.py
from django.shortcuts import render
from .utils import fetch_campus_users
from django.conf import settings  # settings'ten UID ve SECRET almak için
from .forms import UserSearchForm 

def campus_users_view(request):
    users = fetch_campus_users()  # Kullanıcıları API'den çek
    search_results = []

    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_term'].lower()
            search_results = [user for user in users if search_query in user['login'].lower()]
    else:
        form = UserSearchForm()

    return render(request, 'index.html', {'form': form, 'search_results': search_results})