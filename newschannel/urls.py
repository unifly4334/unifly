"""newschannel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from webnews import views
from django.views.generic import RedirectView

from django.conf.urls.static import static

from django.conf import settings

from django.contrib.auth import views as auth_views
""" password reset functions """



urlpatterns = [
  	path('admin/',admin.site.urls),
	path('subpage/<str:title>/',views.subpage,name='sub'),
	path('main/',views.mainpage,name='main'),
	path('national/',views.national,name='national'),
	path('international/',views.international,name='international'),
	path('local/',views.local,name='local'),
	path('cinema/',views.cinema,name='cinema'),
	path('sports/',views.sports,name='sports'),
	path('application/',views.application_view,name='application'),
	path('adminconsole/',views.admin_view,name='adminconsole'),
	path('track/',views.track_view,name='track'),
	path('signup/', views.signup_view, name='signup'),
	path('', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('submit_application/', views.submit_application, name='submit_application'),
	path('update/<int:appid>/',views.update_view,name='update'),
	path('view_app/<int:appid>/',views.view_app,name='view_app'),
    #path('accounts/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('contact/', views.contact_view, name='contact'),
    path('aboutus/', views.aboutus_view, name='aboutus'),


	path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name='reset_password'),

	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name='password_reset_done'),

	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),

	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
