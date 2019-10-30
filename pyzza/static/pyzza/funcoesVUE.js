     /*aqui criamos as estancias do vue*/
    var app = new Vue({

        el:'#app',
        delimiters: ["[[", "]]"],

        /*todos meus dados que seria O array JSON, temos 2 array*/
        data:{
            pizzas : [],
            pizzas_selecionadas:[],
            bebidas:[],
            bebidas_selecionadas:[],
            tamanhos:[],
            tamanhos_selecionados:[],
        },
        /*quando gera a pagina, dentro temos uma funcao que sera executada quando a pagina for criada
        * podemos inserir todas as funcoes que quisermos executar qndo a pagina for criada.*/
        created:function () {
              this.busca_pizzas();
              this.busca_bebidas();
              this.busca_tamanhos();
        },
        monted:function () {

            /*tudo que colocar aqui eh executado a pagina for montada*/
        },
        updated: function(){

        },
        methods: {

            adicionar_pizza: function(pizza){
                this.pizzas_selecionadas.push(pizza);
            },

                  /*busca as pizzas na api*/
            busca_pizzas: function () {
              this.$http.get('/api/pizza/').then(dados => {
                  this.pizzas = dados.body;
             })
            },

            /*funcao que remove as pizzas da comanda.*/
            remover_pizza: function (pizza) {
                this.pizzas_selecionadas = this.pizzas_selecionadas.filter(x => x.id != pizza.id);
            },

              //Busca bebidas na API
               busca_bebidas: function () {
              this.$http.get('/api/bebida/').then(dados => {
                  this.bebidas = dados.body;
             })
            },
                   /*recebe o obj e add na lista*/
            adicionar_bebidas: function (bebidas) {
                this.bebidas_selecionadas.push(bebidas);
            },

            /*funcao que remove as pizzas da comanda.*/
            remover_bebidas: function (bebidas) {
                this.bebidas_selecionadas = this.bebidas_selecionadas.filter(x => x.id != bebidas.id);
            },

            busca_tamanhos: function () {
                this.$http.get('/api/tamanho_pizza/').then(dados => {
                    this.tamanhos = dados.body;
                })
            },

        }
    })

//ABRE MODAL SELECIONADO DE ACORDO COM O TAMANHO ESCOLHIDO
$('#modalUmSabor').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Botão que acionou o modal
  var recipient = button.data('whatever') // Extrai informação dos atributos data-*
  var modal = $(this)
  modal.find('.modal-title').text(recipient)
  modal.find('.modal-body input').val(recipient)
})

$('#modalbebidas').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Botão que acionou o modal
  var recipient = button.data('whatever') // Extrai informação dos atributos data-*
  var modal = $(this)
  modal.find('.modal-title').text(recipient)
  modal.find('.modal-body input').val(recipient)
})
  $('#modalTamanhoPizza').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Botão que acionou o modal
  var recipient = button.data('whatever') // Extrai informação dos atributos data-*
  var modal = $(this)
  modal.find('.modal-title').text(recipient)
  modal.find('.modal-body input').val(recipient)
})
/*
     $('#exampleModal3').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Botão que acionou o modal
  var recipient = button.data('whatever') // Extrai informação dos atributos data-*
  var modal = $(this)
  modal.find('.modal-title').text('3 sabores: ' + recipient)
  modal.find('.modal-body input').val(recipient)
})

 */