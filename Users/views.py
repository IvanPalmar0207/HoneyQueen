from django.shortcuts import render, HttpResponse
#User Model
from Users.models import User
#Regex validation
import re
#Sweetify
import sweetify

#Crete a new User
def registerUser(request):
        if request.method == 'POST':
            documentNumber = request.POST['documentNumber']
            namesUser = request.POST['namesUser']
            emailUser = request.POST['emailUser']
            passwordUser = request.POST['passwordUser']

            #Pattern Email
            patternEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            validationEmail = re.fullmatch(patternEmail, emailUser)

            #Pattern Password
            patternPassword = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
            validationPassword = re.fullmatch(patternPassword, passwordUser)


            if(len(documentNumber) > 10 or len(documentNumber) < 10):               
               sweetify.error(request,'El número de documento no puede tener menos de 10 caracteres ni mas de 10 caracteres, intenta nuevamente.')
            
            elif(namesUser.isdigit()):                
                sweetify.error(request,'El nombre completo del usuario no puede tener numeros, intenta nuevamente.')

            elif(len(emailUser) < 20 or len(emailUser) > 100):                
                sweetify.error(request,'El correo electronico del usuario no puede tener menos de 20 caracteres ni más de 100 caracteres, intenta nuevamente.')

            elif(bool(validationEmail) == False):            
                sweetify.error(request,'El correo ingresado no es un correo valido, intenta nuevamente.')

            elif(len(passwordUser) < 8 or len(passwordUser) > 20):                
                sweetify.error(request,'La contraseña no debe de tener menos de 8 caracteres ni mas de 20 caracteres, intenta nuevamente.')

            elif(bool(validationPassword) == False):                
                sweetify.error(request,'La contraseña no es una contraseña valida, intenta nuevamente')

            else:
                user = User.objects.create(documentNumber = documentNumber, fullName = namesUser, email = emailUser, password = passwordUser)
                user.save()

                sweetify.success(request,'El nuevo usuario ha sido registrado con exito, gracias e inicia sesión.')
                return render(request,'login.html')