from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView #tambien: from django.views.generic.base import View
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(View):

    def get(self, request, *args, **kwargs):

        posts = Post.objects.all()

        context = {

            'posteos' : posts
            
        }
        
        return render(request, 'blog_list.html', context)
    
class BlogCreateView(View):

    def get(self, request, *args, **kwargs):

        formulario = PostCreateForm()

        context = {
            
            'form' : formulario

        }
        
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):

        if request.method == "POST":

            formulario = PostCreateForm(request.POST)

            if formulario.is_valid():
                
                title = formulario.cleaned_data.get('title')
                content = formulario.cleaned_data.get('content')

                publicar, crear = Post.objects.get_or_create(title=title, content=content)
                publicar.save
                
                return redirect('blog:home')
        
        context = {
            
        }
        
        return render(request, 'blog_create.html', context)

class BlogDetailView(View):

    def get(self, request, pk, *args, **kwargs):

        post = get_object_or_404(Post, pk=pk)

        context = {

            'posteo' : post

        }

        return render(request, 'blog_detail.html', context)

class BlogUpdateView(UpdateView):
    
    model = Post
    fields=['title', 'content']
    template_name='blog_update.html'

    def get_success_url(self):
        
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detalles', kwargs={'pk':pk})

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog:home')
