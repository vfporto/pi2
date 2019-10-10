 /*para pegar se eh grande pequena grande*/
 $('#exampleModal').on('show.bs.modal', function (event) {
     var button = $(event.relatedTarget) // Botão que acionou o modal
     var recipient = button.data('whatever') // Extrai informação dos atributos data-*
     var modal = $(this)
     modal.find('.modal-title').text('2 Sabores ' + recipient)
     modal.find('.teste').val(recipient)
 })

 /*funcao buscar*/
 $('input#txt_consulta').quicksearch('table#exampleModal modal-body p');


 /*abrir modals*/

$(document).ready(function () {
    $('#abrir').click(function () {
        $('#myModal').modal({
            show: true
        })
    });
        $(document).on('show.bs.modal', '.modal', function (event) {
            var zIndex = 1040 + (10 * $('.modal:visible').length);
            $(this).css('z-index', zIndex);
            setTimeout(function() {
                $('.modal-backdrop').not('.modal-stack').css('z-index', zIndex - 1).addClass('modal-stack');
            }, 0);
        });
});

function finalizarPedido() {


}
 function teste() {
     alert('vai voltar memô tio? fica ae poha!!!!');
 }
