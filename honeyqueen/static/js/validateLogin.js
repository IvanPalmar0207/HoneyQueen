function validateLogin(){
    var documentNumber = document.form.documentNumber.value
    var email = document.form.email.value
    var password = document.form.password.value

    //Validations

    let lowerCase = /[a-z]/g
    let upperCase = /[A-Z]/g
    let patternEmail = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
    let patternPassword = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$/

    if(documentNumber.length > 10 || documentNumber.length < 10){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El número de documento no puede tener menos ni más de 10 caracteres, intenta nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false       
    }

    else if(documentNumber.match(lowerCase) || documentNumber.match(upperCase)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El numero de documento no puede contener ni letras mayusculas ni letras minusculas, intenta nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
    }

    else if(email.length < 20 || email > 100){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El correo electronico no puede tener menos de 20 caracteres ni más de 100 caracteres, intenta nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
    }

    else if(!patternEmail.test(email)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El correo electronico no es valido, intenta nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
    }

    else if(password.length < 8 || password.length > 20){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La contraseña no puede tener menos de 8 caracteres ni mas de 20 caracteres, intenta nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
    }

    else if(!patternPassword.test(password)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La contraseña no es valida por favor intentalo nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
    }

    else{
        return true
    }

}