from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from pickee_api import views

page_urls = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("vue_app_01/", TemplateView.as_view(template_name="vue_app_01.html"), name="vue_app_01"),
    path("vue_app_02/", TemplateView.as_view(template_name="vue_app_02.html"), name="vue_app_02"),
    path("login/", views.user_login, name='login'),
    path("signup/", views.user_signup, name='signup')
]

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('pickee_api.urls')),
              ] + page_urls
