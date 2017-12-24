from django.urls import path

from .views import *

urlpatterns = [
    path('', new_topic, name='home'),
    path('post/<int:pk>/edit', EditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', DeleteView.as_view(), name='post_delete'),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
]
	