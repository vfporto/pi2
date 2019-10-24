     /*aqui criamos as estancias do vue*/
    var app = new Vue({

        el:'#app',
        delimiters: ["[[", "]]"],

        /*todos meus dados que seria O array JSON, temos 2 array*/
        data:{
            UmSaborLimite: false,
            UmSaborLimiteClick: 1,
            DoisSaborLimite: false,
            DoisSaborLimiteClick: 2,
            TresSaborLimite: false,
            TresSaborLimiteClick: 3,
            pizzas : [],
            pizzas_selecionadas:[],
            bebidas:[],
            bebidas_selecionadas:[],
        },
        /*quando gera a pagina, dentro temos uma funcao que sera executada quando a pagina for criada
        * podemos inserir todas as funcoes que quisermos executar qndo a pagina for criada.*/
        created:function () {
              this.busca_pizzas();
              this.busca_bebidas();
        },
        monted:function () {

            /*tudo que colocar aqui eh executado a pagina for montada*/
        },
        updated: function(){
          // console.log(this.pizzas_selecionadas);
          //   console.log('pizzas_selecionadas');
        },
        methods: {

            //para limitar a quantidade de click dependendo do sabor
            limitaEscolhaSabor(){
                if(this.UmSaborLimiteClick == 0) {
                    this.UmSaborLimite = true;
                } else {
                    this.UmSaborLimiteClick--;
                }
            },
              limitaEscolherDoisSabores(){
                if(this.DoisSaborLimiteClick == 0) {
                    this.DoisSaborLimite = true;
                } else {
                    this.DoisSaborLimite--;
                }
            },
              limitaEscolherTresSabores(){
                if(this.TresSaborLimiteClick == 0) {
                    this.TresSaborLimite = true;
                } else {
                    this.TresSaborLimite--;
                }
            },


                  /*busca as pizzas na api*/
            busca_pizzas: function () {
              this.$http.get('/api/pizza/').then(dados => {
                  this.pizzas = dados.body;
             })
            },

            /*recebe o obj e add na lista*/
            adicionar_pizza: function (pizza) {
                this.limitaEscolhaSabor()
                if(this.UmSaborLimite == false) {
                    this.pizzas_selecionadas.push(pizza);
                } else {
                    // console.log('nao pode mais adicionar pizzas'    );
                    alert('Você só pode adicionar 1 sabor. Escolha Fechar, Finalizar Pedido ou Escolha uma Bebida!');
                }
            },
            adicionar_pizza_dois_sabores: function(pizza){
                this.limitaEscolherDoisSabores()
                if (this.DoisSaborLimite == false){
                    this.pizzas_selecionadas.push(pizza);
                }else{
                     // console.log('nao pode mais adicionar pizzas'    );
                    alert('Você só pode adicionar 2 sabor. Escolha Fechar, Finalizar Pedido ou Escolha uma Bebida!');
                }
            },
            adicionar_pizza_tres_sabores: function(pizza){
                this.limitaEscolherTresSabores()
                if (this.TresSaborLimite == false){
                    this.pizzas_selecionadas.push(pizza);
                }else{
                     // console.log('nao pode mais adicionar pizzas'    );
                    alert('Você só pode adicionar 3 sabor. Escolha Fechar, Finalizar Pedido ou Escolha uma Bebida!');
                }
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
            adicionar_bebidas: function (bebida_id, tamanho_id) {
                console.log("bebida_id: "+bebida_id);
                console.log("tamanho_id: "+tamanho_id);
                this.bebidas_selecionadas.push("Bebida "+bebida_id+", "+tamanho_id);
                localStorage.setItem('bebidas', JSON.stringify(this.bebidas_selecionadas));
            },

            /*funcao que remove as pizzas da comanda.*/
            remover_bebidas: function (bebidas) {
                this.bebidas_selecionadas = this.bebidas_selecionadas.filter(x => x.id != bebidas.id);
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