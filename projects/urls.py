from django.urls import path
from projects import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('machine', views.machine, name='machine'),
    path('hardware',views.hardwares, name= 'hardware'),
    path('python', views.python, name ='python'),
    path('titanic',views.titanic, name = 'titanic'),
    path('iris',views.iris, name ='iris'),
    path('titanicresult/',views.titanicresult, name = 'titanicresult'),
    path('irisresult/',views.irisresult, name = 'irisresult'),
    path('houseprice',views.house,name = 'house'),
    path('houseresult',views.houseresult,name ='houseresult'),
    path('cancer',views.cancer,name = 'cancer'),
    path('c_result',views.cancerresult,name ='c_result'),
    path('sentiment',views.sentiment,name='sentiment'),
    path('sentimentresult',views.sentimentresult, name='sentimentresult'),
    path('Blogs/<project_id>',views.pythonblog, name ='blogs'),
    path('Blog/<project_id>',views.hardwareblog, name ='blog'),

]







if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 