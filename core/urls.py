from django.urls import path,include
from . import views

app_name='core'

urlpatterns = [
    path('',views.FormView,name='Home'),
    path('result/',views.FormData,name='Result'),
    path('render/pdf/',views.Pdf.as_view(),name='pdf'),
]