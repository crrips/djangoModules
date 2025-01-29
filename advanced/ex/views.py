from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .models import Article, UserFavouriteArticle, User
from django.contrib.auth.forms import UserCreationForm
from .forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy


class Home(ListView):
    model = Article
    template_name = "ex/home.html"
    context_object_name = 'articles'
    ordering = ['-created']
        

class Login(ListView):
    model = Article
    template_name = "ex/home.html"
    context_object_name = 'articles'
    ordering = ['-created']
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('home')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home') 


class Publications(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    
    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(author=request.user).order_by('-created')
        return render(request, 'ex/publications.html', {'articles': articles})
    
    
class ArticleDetail(DetailView):
    model = Article
    template_name = 'ex/article_detail.html'
    context_object_name = 'article'


class Logout(TemplateView):
    template_name = 'ex/home.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('home')
        

class Favourites(LoginRequiredMixin, ListView):
    model = UserFavouriteArticle
    template_name = 'ex/favourites.html'
    context_object_name = 'favourites'
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        favourites = UserFavouriteArticle.objects.filter(user=self.request.user).values_list('article', flat=True)
        return Article.objects.filter(id__in=favourites).order_by('-created')


class Register(CreateView):
    form_class = UserCreationForm
    template_name = "ex/register.html"
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field.capitalize()}: {error}")
        return self.render_to_response(self.get_context_data(form=form))
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    
class Publish(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'ex/publish.html'
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return redirect('home')
    
    
class AddFav(LoginRequiredMixin, CreateView):
    model = UserFavouriteArticle
    template_name = 'ex/article_detail.html'
    login_url = reverse_lazy('login')
    
    def post(self, request, *args, **kwargs):
        user = request.user
        article_id = request.POST.get('article_id')
        
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
                if self.model.objects.filter(user=user, article=article).exists():
                    return HttpResponse("Article already in favourites", status=400)
                self.model.objects.get_or_create(user=user, article=article)
            except Article.DoesNotExist:
                print(f"Article with ID {article_id} does not exist.")

        return redirect('favourites')

