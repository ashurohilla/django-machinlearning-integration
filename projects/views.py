import string
from django.shortcuts import render
from . import prediction
from projects.models import project
from projects.models import hardware
# Create your views here.
data ={}
def machine(request):
    return render (request, 'templates/projects/machinelearning/machine.html')

   
def hardwares (request):
    projectdata = hardware.objects.all()
    data ={
        'projectdata':projectdata,

    }
    return render ( request, 'templates/projects/hardware/hardware.html',data)

         
def python (request):
    projectdata = project.objects.all()
    data ={
        'projectdata':projectdata,

    }

    return render ( request, 'templates/projects/pythonprojects/python.html',data)  
def titanic(request):
    return render (request, 'templates/projects/machinelearning/titanic/titanic.html')
# our result page view
def titanicresult(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])

    titanicresult = prediction.getPredictions(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)

    return render(request, 'templates/projects/machinelearning/titanic/titanicresult.html', {'titanicresult':titanicresult})  
def iris(request):

    return render(request, 'templates/projects/machinelearning/iris/iris.html')

def irisresult(request):
    sepallength = int(request.GET['sepallength'])
    sepalwidth = int(request.GET['sepalwidth'])
    petallength = int(request.GET['petallength'])
    petalwidth = int(request.GET['petalwidth'])

    irisresul = prediction.getpredictioniris(sepallength, sepalwidth, petallength, petalwidth)
    return render(request,'templates/projects/machinelearning/iris/irisresult.html', {'irisresul':irisresul})
def house(request):

    return render(request,'templates/projects/machinelearning/housepriceprediction/house.html')    

def houseresult(request):
    total_sqft = int(request.GET['total_sqft'])
    balconies = int(request.GET['balconies'])
    bathroom = int(request.GET['bathroom'])
    bhk = int(request.GET['bhk'])
    Area = string(request.GET['Area'])
    location = string(request.GET['location'])

    houseresult =prediction.get_predicted_price(total_sqft, balconies,bathroom,bhk, Area, location)

    return render(request, 'templates/projects/machinelearning/housepriceprediction/houseresult.html',{'houseresult' :houseresult})
def cancer(request):
    return render(request, 'templates/projects/machinelearning/cancerprediction/cancer.html')   

def cancerresult(request):
    
    return render(request, 'templates/projects/machinelearning/cancerprediction/c_result.html')     
def sentiment(request):

    return render(request,'templates/projects/machinelearning/sentimentanalyzer/sentiment.html') 

def sentimentresult(request):
    return render (request,'templates/projects/machinelearning/sentimentanalyzer/sentimentresult.html') 
def pythonblog(request,project_id):
    projectdata = project.objects.get(project_id=project_id)
    blogdata ={
        'projectdata':projectdata, 
    }
    return render (request,'templates/Blogs.html',blogdata)

def hardwareblog(request,project_id):
    projectdata = hardware.objects.get(project_id=project_id)
    hardwaredata ={
        'projectdata':projectdata, 
    }
    return render (request,'templates/hardwareblogs.html',hardwaredata)