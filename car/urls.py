from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('booking/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('team/', views.team, name='team'),
    path('login/', views.login, name='login'),
    path('list/', views.list, name='list'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
    path('update/<int:post_id>', views.update, name='update'),
    path('delete/<int:post_id>', views.delete, name='delete'),
]