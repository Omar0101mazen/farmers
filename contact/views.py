from django.shortcuts import render
from . models import message
# Create your views here.
def send_message(request):
    if request.method == 'POST':
        names = request.POST['name']
        emails = request.POST['email']
        messsage = request.POST['message']
        send = message(name = names ,email= emails ,messsage = messsage)
        send.save()

        
        
            
    return render(request,'contact/contact.html')