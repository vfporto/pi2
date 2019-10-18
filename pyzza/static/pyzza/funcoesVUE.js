     /*aqui criamos as estancias do vue*/
    var app = new Vue({

        el:'#app',
        delimiters: ["[[", "]]"],

        /*todos meus dados que seria O array JSON, temos 2 array*/
        data:{
            pizzas : [],
            pizzas_selecionadas:[],
        },
        /*quando gera a pagina, dentro temos uma funcao que sera executada quando a pagina for criada
        * podemos inserir todas as funcoes que quisermos executar qndo a pagina for criada.*/
        created:function () {
              this.busca_pizzas();
        },
        monted:function () {
             /*tudo que colocar aqui eh executado a pagina for montada*/
        },
        methods: {

            /*busca as pizzas na api*/
            busca_pizzas: function () {
              this.$http.get('/api/pizza/').then(dados => {
                  this.pizzas = dados.body;
             })
            },

            /*recebe o obj e add na lista*/
            adicionar_pizza: function (pizza) {
                this.pizzas_selecionadas.push(pizza);
            },

            /*funcao que remove as pizzas da comanda.*/
            remover_pizza: function (pizza) {
                this.pizzas_selecionadas = this.pizzas_selecionadas.filter(x => x.id != pizza.id);
            }

        }
    })

//ABRE MODAL SELECIONADO DE ACORDO COM O TAMANHO ESCOLHIDO
$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Botão que acionou o modal
  var recipient = button.data('whatever') // Extrai informação dos atributos data-*
  var modal = $(this)
  modal.find('.modal-title').text('Tamanho escolhido: ' + recipient)
  modal.find('.modal-body input').val(recipient)
})

$('#exampleModal2').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Botão que acionou o modal
  var recipient = button.data('whatever') // Extrai informação dos atributos data-*
  var modal = $(this)
  modal.find('.modal-title').text('2 sabores: ' + recipient)
  modal.find('.modal-body input').val(recipient)
})

     $('#exampleModal3').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Botão que acionou o modal
  var recipient = button.data('whatever') // Extrai informação dos atributos data-*
  var modal = $(this)
  modal.find('.modal-title').text('3 sabores: ' + recipient)
  modal.find('.modal-body input').val(recipient)
})