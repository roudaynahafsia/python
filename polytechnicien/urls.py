from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('members/<int:member_id>', views.members, name='members'),
    path('add/', views.add, name='add'),
    path('addmen/', views.add_member, name='addmen'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/upmen/<int:id>', views.update_member, name='upmen'),
    path('api/student/', views.MemberView.as_view(), name='student_api'),
    path('api/student/<int:id>', views.MemberView.as_view(), name='student_api_detail'),  
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register')
]