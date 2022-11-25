from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TodoListView(LoginRequiredMixin, ListView):
    model = TodoModel
    template_name = 'Todo/home.html'
    context_object_name = 'Todos'

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        context['Todos'] = context['Todos'].filter(author = self.request.user)
        context['count'] = context['Todos'].filter(complete = False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['Todos'] = context['Todos'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        
        return context

        
class TaskDetailView(DetailView):
    model = TodoModel
    template_name = 'Todo/detail.html'
    context_object_name = 'tasks'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TodoModel
    template_name = 'Todo/create-View.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoModel
    template_name= 'Todo/Update.html'
    fields = [ 'title', 'description', 'complete']
    success_url = reverse_lazy('home')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoModel
    template_name = 'Todo/delete.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('home')

    

