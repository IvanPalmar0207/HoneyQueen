from django.http import HttpResponse
from django.shortcuts import redirect
#User Model
from Users.models import User
#Authenticate
from django.contrib.auth import authenticate
#Messages
from django.contrib import messages

#Crete a new User
def registerUser(request):
    try:
        if request.method == 'POST':
            documentNumber = request.POST['documentNumber']
            namesUser = request.POST['namesUser']
            emailUser = request.POST['emailUser']
            passwordUser = request.POST['passwordUser']            

            if User.objects.filter(documentNumber = documentNumber):
                messages.info(request,'El usuario ya existe, trata de iniciar sesión.')
                return redirect(to = 'login')    

            else:
                user = User.objects.create(documentNumber = documentNumber, fullName = namesUser, email = emailUser)
                user.set_password(passwordUser)
                user.save()
                messages.success(request,'El usuario ha sido guardado correctamente.')
                return redirect(to = 'login')                     
    except:
        pass

def loginUser(request):
    if request.method == 'POST':
        documentNumber = request.POST['documentNumber']
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

    if user is None:
        return HttpResponse('Puta')
    else:
        return HttpResponse('Hola')