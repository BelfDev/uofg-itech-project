from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from pickee_api import views

page_urls = [
    path("", views.home, name="home"),
    path("recommendation/", views.recommendation, name="recommendation"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("login/", views.user_login, name='login'),
    path("signup/", views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path("profile/", TemplateView.as_view(template_name="profile_main.html"), name='profle_main'),
    path("preferences/", TemplateView.as_view(template_name="profile_preferences.html"), name='profile_preferences'),
    path("history/", TemplateView.as_view(template_name="profile_history.html"), name='profile_history')
]

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('pickee_api.urls')),
              ] + page_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
