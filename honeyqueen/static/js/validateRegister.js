function validateRegister(){
    var documentNumber = document.form.documentNumber.value
    var namesUser = document.form.namesUser.value
    var emailUser = document.form.emailUser.value
    var passwordUser = document.form.passwordUser.value

    //Validations

    let lowerCase = /[a-z]/g
    let upperCase = /[A-Z]/g


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

    else if(namesUser.match(lowerCase) ){
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

}