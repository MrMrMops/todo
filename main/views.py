from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from rest_framework import viewsets

from .forms import TodoAddPageForm, LoginUserForm, RegisterForm, ProfileForm
from .models import todo, Profile
from .serializers import TodoSerializer

class TodoViewset(viewsets.ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer

class IndexView(ListView):
    model = todo
    template_name = 'main/index.html'
    context_object_name = 'todolist'

    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'TodoList'
        profiles = Profile.objects.all()

        if self.request.user.is_authenticated :
            link = profiles.get(user_id=self.request.user.id).pk
            context['link'] = link

        return context


class SelfView(ListView):
    model = todo
    template_name = 'main/index.html'
    context_object_name = 'todolist'

    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'SelfList'
        profiles = Profile.objects.all()
        if self.request.user.is_authenticated:
            link = profiles.get(user_id=self.request.user.id).pk
            context['link'] = link

        return context
    def get_queryset(self):
        todos = todo.objects.all()
        todolist = todos.filter(user=self.request.user)
        return todolist

class TodoPageView(DetailView):
    model = todo
    template_name = 'main/page.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

class TodoDeleteView(DeleteView):
    model = todo
    success_url = reverse_lazy('index')
    template_name = 'main/delete.html'

class TodoAddPageView(CreateView):
    model = todo
    template_name = 'main/addtodo.html'
    form_class = TodoAddPageForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('index')

def LogoutUserView(request):

    logout(request)
    return redirect('index')
class ShowProfileView(DetailView):
    model = Profile
    template_name = 'main/showprofile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user

        if self.request.user.is_authenticated :
            profiles = Profile.objects.all()
            link = profiles.get(user_id=self.request.user.id).pk
            context['link'] = link

        return context


class  UpdateProfileView(UpdateView):
    model = Profile
    fields = ['avatar', 'bio', ]
    template_name = 'main/createprofile.html'

class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if register_form.is_valid() or profile_form.is_valid():

            user = register_form.save()
            login(self.request,user)

            profile = profile_form.save()
            profile.user = request.user
            profile.save()


            return redirect('index')
        return HttpResponse('ты хуеосс')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = RegisterForm
        context['form'] = ProfileForm
        return dict(list(context.items()))




