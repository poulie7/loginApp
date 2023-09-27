from django.urls import path
from .views import ArticleView, RegisterView, LoginView, LogoutView

urlpatterns = [
	path("article", ArticleView.as_view()),
	path("register", RegisterView.as_view()),
	path('login/', LoginView.as_view()),
	path('logout/', LogoutView.as_view()),


]
