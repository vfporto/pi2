/*END MENU LATERAL*/
 let headers = {
            'Content-Type': 'application/json;charset=utf-8',
            "X-CSRFToken": token
          };

 /*
document.HTMLElement = function (selecionada) {
    return selecionada;
}
*/

function pizza_escolhida() {
     var selecionada = document.getElementById("titulo");
     let pizza =new Array()
        //converte strings para um objeto e coloca no localstorage
        if(localStorage.hasOwnProperty("pizza")){
            pizza = JSON.parse(localStorage.getItem(pizza) || '[]');
        }
     selecionada.addEventListener('click', function () {
         console.log(selecionada);

     });

  }


