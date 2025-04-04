from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = "blog"

urlpatterns = [
    
    path('', BlogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="crear"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detalles"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="actualizar"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="eliminar")
    
]