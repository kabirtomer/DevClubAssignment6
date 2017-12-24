from django.urls import path

from .views import *

urlpatterns = [
    path('', new_topic, name='blogs'),
    path('post/<int:pk>/edit', BlogEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
]
