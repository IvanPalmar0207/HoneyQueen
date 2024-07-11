let counter = 0

const counterValue = document.getElementById('counterValue')
const incrementBtn = document.getElementById('incrementBtn')
const decrementBtn = document.getElementById('decrementBtn')

incrementBtn.addEventListener('click',()=>{
    counter++;
    counterValue.innerHTML = counter;
    if(counter <= 0){
        counterValue.innerHTML = 1;
    }
})

decrementBtn.addEventListener('click', () => {
    counter--;
    counterValue.innerHTML = counter;
    
    if(counter <= 0){
        counterValue.innerHTML = 1;
    }
})