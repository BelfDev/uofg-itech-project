from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from pickee_api import views

page_urls = [
    path("", views.home, name="home"),
    path("recommendation/", views.recommendation, name="recommendation"),
    path("about/", views.about, name="about"),
    path("login/", views.user_login, name='login'),
    path("signup/", views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path("profile/", views.profile, name="profile"),
    path("preferences/", views.preferences, name="preferences"),
    path("history/", views.history, name="history"),
]

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('pickee_api.urls')),
              ] + page_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
