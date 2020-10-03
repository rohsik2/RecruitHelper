from django.shortcuts import render, get_object_or_404
from .models import Service, Cutline
from .forms import ServiceForm


def service_list(request):
    services = Service.objects.all()
    return render(request, 'serviceapply/service_list.html', {'services': services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    cutlines = Cutline.objects.filter(service=service).order_by('-date')
    date = []
    data = []
    for cutline in cutlines:
        temp = str(cutline.date)
        date.append(int(temp[5:7]))
        data.append(cutline.score)
    return render(request, 'serviceapply/service_detail.html', {'service': service, 'datas': data, 'dates':date})

