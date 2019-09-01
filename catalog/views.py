from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse

from .models import User, Book
from .forms import UserForm


class UserListView(generic.ListView):
    queryset = User.objects.filter(is_staff='False')
    template_name = 'index.html'


class UserDetailView(generic.DetailView):
    model = User


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'genre', ]

    def get_success_url(self):
        return reverse('user-detail', kwargs={'pk': self.object.user.pk})


class BookCreateView(CreateView):
    model = Book
    fields = ['user', 'title', 'author', 'genre', ]

    def get_success_url(self):
        return reverse('user-detail', kwargs={'pk': self.object.user.pk})


class UserCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': UserForm}
        return render(request, 'catalog/user_form.html', context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return HttpResponseRedirect(reverse('user-detail', args=[user.pk]))
        return render(request, 'catalog/user_detail.html', {'form': form})
