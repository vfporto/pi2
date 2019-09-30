/*MENU LATERAL*/
$('.btn-expand-collapse').click(function(e) {
				$('.navbar-primary').toggleClass('collapsed');
});
/*END MENU LATERAL*/

/*MEU ARRAY DE PIZZAS*/
var arrayPizza = new Array("calabresa","peperoni","mussarela","tomate-seco");

var options = ["1", "2", "3", "4", "5"];
$('#pizzasEscolha').empty();
$.each(options, function(i, p) {
    $('#pizzasEscolha').append($('<select></select>').val(p).html(p));
});