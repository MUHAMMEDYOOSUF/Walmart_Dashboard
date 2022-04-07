from django.db.models import Sum, Avg
from django.shortcuts import render, redirect

# Create your views here.
from DashWalmartApp.forms import DataForm
from DashWalmartApp.models import my_ml, data


def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prediction')
    else:
        form=DataForm()


    return render(request,'index.html',{'form':form})

def prediction(request):
    prediction=my_ml.objects.all()
    return render(request,'prediction.html',{'prediction':prediction})


def new(request):
    # d=[]
    # t=[]
    l=[*range(1,46)]
    w=[*range(1,53)]
    # for i in range(1,46):
    #     d.append(data.objects.filter(Store=i).aggregate(Avg('Weekly_Sales'))['Weekly_Sales__avg'])
    #
    # for i in range(1,46):
    #     t.append(data.objects.filter(Store=i).aggregate(Sum('Weekly_Sales'))['Weekly_Sales__sum'])
    #
    #
    #
    # return render(request,'new.html',{'labels':l,'datas':d,'total':t})
    total=[222297882,275346381,57550471,299498625,45414494,223665111,81563258,129913067,77776638,271506130,193915867,144233109,286439590,288933861,89069305,74219626,127715038,155077283,206552941,301341212,108077119,147032013,198726489,193959322,100990243,143391991,253786086.,189210536,77112153,62672882,199565742,166754073,37128679,138231090,131485699,53388879,74159123,55125508,207397918,137830556,181284401,79533395,90537744,43258377,112359590]
    return render(request, 'new.html', {'labels': l, 'total': total,'weeks':w})