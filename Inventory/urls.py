from django.urls import path
from interface import views
from item.views import ItemChartView

urlpatterns = [
    path('', views.cover, name='cover'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('categories', views.categories, name='categories'),
    path('check', views.check, name='check'),
    path('arsenal', views.arsenal, name='arsenal'),
   # path('', ItemChartView.as_view(), name='home'),
    path('chart', ItemChartView.as_view(), name = 'chart')

]
