from django.urls import include,path
from django.conf.urls import  url

from .views import HomeView,FormView
from .import views

  
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static


from django.urls import reverse_lazy
  

from django.contrib.auth import views as auth_views
1

app_name= "animalpre"

router = routers.DefaultRouter()
router.register('animalpre', views.AnimalfeaturesView)

urlpatterns = [
    url(r'^$', views.HomeView, name="home"),

    url(r'^login/$', views.LoginView.as_view(), name='login'),

    url(r'^animalnews/$', views.HomeNewsView, name="newsfeed"),

    url(r'^animalposted/(?P<pk>[0-9]+)/$', views.apianimaldetail, name='apidetail'),

    

    url(r'^form/$', views.FormViews, name="form"),

    url(r'^predict/$', views.FormViews2, name="predictform"),

    url(r'^apicontent/$', views.apistuff, name="apistuff"),

    

    url(r'^apicontent2/$', views.apistuff2, name="apistuff2"),

    url(r'^signup/$', views.usersignup, name="signup"),

    url(r'^thanksforregister/$', views.thanksregister, name="thanksforreg"),

    url(r'^registersucess/$', views.successregister, name="successregister"),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='profile'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    views.activate_account, name='activate'),

    path('api/', include(router.urls), name='api'),
    
    
    path('status/', views.prediction),

   

#change password

     url(r'^animalpre/password_reset/$', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('animalpre:password_reset_done')), {'template_name': 'animalpre/reset_password.html', 'post_reset_redirect': 'animalpre:password_reset_done', 'email_template_name': 'animalpre/reset_password_email.html'}, name='reset_password'),

    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name= 'animalpre/reset_password.html',email_template_name= 'animalpre/reset_password_email.html', success_url=reverse_lazy('animalpre:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'animalpre/reset_password_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'animalpre/reset_password_confirm.html', success_url=reverse_lazy('animalpre:password_reset_complete')), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'animalpre/reset_password_complete.html'), name='password_reset_complete'),
    
]

