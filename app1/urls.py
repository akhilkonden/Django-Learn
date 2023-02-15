from django.urls import path
from . import views
urlpatterns = [
    path('', views.page1,name = "home page"),
    path('2/',views.page2,name = "home2"),
    path('3/',views.page3,name = "home3"),
    # path('4/',views.page4,name = "home4"),
    path('5/',views.page5,name = "home5"),
    path('6/',views.form1,name = "home6")

]
