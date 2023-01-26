
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Folder

# Create your views here.
#def patient_detail(request, id):
#    obj = get_object_or_404(Folder, id=id)
#    context = {'dd': obj}
#   return render(request, "file_patient.html", context)
def patient_detail(request):
    obj = Folder.objects.all()
    context = {"obj": obj}
    return render(request, "file_patient.html", context)

def patientView(request):
    if request.method == 'POST':
        date_registered = request.POST['date_registered']
        first_name = request.POST['first_name']
        median_name = request.POST['median_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        martial_status = request.POST['martial_status']
        occupation = request.POST['occupation']
        religion = request.POST['religion']
        address = request.POST['address']
        mobile = request.POST['mobile']
        email = request.POST['email']
        relative_name = request.POST['relative_name']
        relative_address = request.POST['relative_address']
        relative_contact = request.POST['relative_contact']
        nhis_number = request.POST['nhis_number']
        
        ins = Folder(date_registered=date_registered, first_name=first_name, median_name=median_name, last_name=last_name, gender=gender, date_of_birth= date_of_birth, martial_status = martial_status,occupation =occupation, religion=religion, address=address,mobile = mobile, email = email, relative_name = relative_name, relative_address= relative_address, relative_contact = relative_contact, nhis_number =nhis_number)
        ins.save()
    my_context={}
    return render(request, "patient.html", my_context)