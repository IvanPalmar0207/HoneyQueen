function validateProducts(){
    let productName = document.form.productName.value
    let productDescription = document.form.productDescription.value
    let productPrice = document.form.productPrice.value
    let productImage = document.form.productImage.value 
    let myCheckBox = document.getElementById('myCheckBox')
    
    let extention = productImage.substring(productImage.lastIndexOf('.', productImage.length))

    //Validations
    let numbers = /[1-9999999999999]/g
    let lowerCase = /[a-z]/g
    let upperCase = /[A-Z]/g

    if(productName.match(numbers)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El nombre del producto no puede contener números, intenta nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
    }

    else if(productName.length < 5 || productName.length > 80){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El nombre del producto no puede tener menos de 5 caracteres ni mas de 80 caracteres, intenta nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
    }

    else if(productDescription.length < 5 || productDescription.length > 150){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La descripción del producto no puede tener menos de 5 caracteres ni mas de 150 caracteres, intenta nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
   }

   else if(productPrice.match(lowerCase) || productPrice.match(upperCase)){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El precio del producto no puede contener letras, ni mayusculas ni minusculas, intenta nuevamente.',
            confirmButtonText: "Atras",
            allowEnterKey:true,
            allowOutsideClick:false,
            confirmButtonColor:"red"
            }
        )
        return false
   }
}