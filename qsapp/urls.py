
from django.conf.urls import url
from qsapp import views

# app namespace Declaration 
# for URls
app_name = "qsapp"


# url routes tp endpoints
urlpatterns = [

    # Url Route for the index/homepage 
    # mapped with the index view/controller
    url(r'^$', views.index, name="index"),

    # Url Route for the answer Endpoint 
    # mapped with correct_answer view/controller
    url(r'^answer/$', views.correct_answer, name="answer"),

]