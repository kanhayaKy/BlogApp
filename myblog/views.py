from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
    #return render(request,'home.html')
    

class home(ListView):
    model = Post
    template_name = 'home.html'
    
    

class post(DetailView):
    model = Post
    template_name = 'post_info.html'
    
    
class create(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class update(UpdateView):
    model = Post
    template_name='update_post.html'
    fields=['title','body']
    
class delete(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
