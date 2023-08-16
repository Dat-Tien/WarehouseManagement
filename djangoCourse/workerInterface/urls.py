from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkerView.workerGet, name='get'),
    path('worker/', views.WorkerView.workerGet, name='create')
    # path('update/<int:id>/', views.update, name='update'),
    # path('detail/<int:id>/', views.detail, name='detail'),
    # path('delete/<int:id>/', views.delete, name='delete'),
]