from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from pickee_api import views

page_urls = [
    path("", TemplateView.as_view(template_name="home.html"), name="index"),
    path("vue_app_01/", TemplateView.as_view(template_name="vue_app_01.html"), name="vue_app_01"),
    path("login/", views.user_login, name='login'),
    path("signup/", views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('pickee_api.urls')),
              ] + page_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
