from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from django.template import loader
from .models import Airlines, Booked_list
from django.http import HttpResponse

def homepage(request):
    myairline=Airlines.objects.all().values('airline_name', 'id', 'airline_model')
    template=loader.get_template('master.html')
    context={
        'myairline':myairline,
    }
    return HttpResponse(template.render(context,request))

def detailairlines(request, id):
    myairline = Airlines.objects.get(id=id)
    template = loader.get_template('flightdetail.html')
    context = {
        'myairline': myairline
    }
    return HttpResponse(template.render(context, request))

def bookedlist(request):
    booked=Booked_list.objects.all().values('id','airline_name','booked_date')
    template=loader.get_template('master.html')
    context={
        'booked':booked,
    }
    return render(context,request)

def bookedlistdetail(request,id):
    booked=Booked_list.objects.get(id=id)
    template=loader.get_template('bookedlistdetail.html')

def confirm_schedule(request, pk):
    airline = get_object_or_404(Airlines, pk=pk)
    if request.method == 'POST' and 'confirm_schedule' in request.POST:
        schedule_date = request.POST.get('schedule_date')
        schedule_time = request.POST.get('schedule_time')
        
        # Save to BookedList
        booked = Booked_list(
            airline=airline,
            schedule_date=schedule_date,
            schedule_time=schedule_time
        )
        booked.save()
        
        return redirect('success_page')  # Redirect to a success page or another view

    return render(request, 'flightdetail.html', {'myairline': airline})