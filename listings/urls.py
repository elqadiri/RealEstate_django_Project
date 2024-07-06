from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('property-list/', views.PropertyList, name='property-list'),
    path('property-type/', views.PropertyType, name='property-type'),
    path('property-agent/', views.PropertyAgent, name='property-agent'),
    path('Testimonial/', views.Testimonial, name='Testimonial'),
    path('property/search/', views.property_search, name='property_search'),
    path('property/search2/', views.property_search2, name='property_search2'),
    path('property-list/for-sale/', views.property_list_for_sale, name='property_list_for_sale'),
    path('property-list/for-rent/', views.property_list_for_rent, name='property_list_for_rent'),
    path('properties/<str:property_type>/', views.properties_by_type, name='properties_by_type'),
    path('annonce/<int:id>/', views.annonce_detail, name='annonce_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

