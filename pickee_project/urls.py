from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from pickee_api.views import auth

page_urls = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("vue_app_01/", TemplateView.as_view(template_name="vue_app_01.html"), name="vue_app_01"),
    path("login/", auth.user_login, name='login'),
    path("signup/", auth.user_signup, name='signup'),
    path('logout/', auth.user_logout, name='logout'),
]

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('pickee_api.urls')),
              ] + page_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
