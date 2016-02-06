from django.conf.urls import include, url
from django.contrib import admin
from pages import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'vervetree.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^Join/', views.Join.as_view(), name='join'),
    url(r'^Scholarship/', views.Scholarship.as_view(), name='scholarship'),
    url(r'^PasswordResset/', views.PasswordResset.as_view(), name='passwordResset'),
    url(r'^ContactForm/', views.ContactForm.as_view(), name='contactForm'),
    url(r'^Prospectus/', views.Prospectus.as_view(), name='prospectus'),
    url(r'^Uni/', views.Uni.as_view(), name='uni'),
    url(r'^PrivacyPolicy/', views.PrivacyPolicy.as_view(), name='privacyPolicy'),
    url(r'^CookiePolicy/', views.CookiePolicy.as_view(), name='cookiePolicy'),
    url(r'^TermsOfService/', views.TermsOfService.as_view(), name='termsOfService'),
    url(r'^UniConnect/', views.UniConnect.as_view(), name='uniConnect'),

]
