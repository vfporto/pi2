     /*aqui criamos as estancias do vue*/

     var exemplo = {
         "itens_pizza": [
             {
                 "id": 3,
                 "quantidade": 2,
                 "pedido": 2,
                 "tamanho_pizza": 1,
                 "sabor_borda": 2,
                 "sabores": [
                     3,
                     4
                 ]
             }
         ],
         "itens_bebida": [
             {
                 "id": 2,
                 "quantidade": 1,
                 "pedido": 2,
                 "bebida_tamanho": 1
             }
         ],
         "troco_para": "0.00",
         "observacao": "",
         "forma_de_pagamento": 1,
         "cliente": 1
     };


    var app = new Vue({

        el:'#app',
        delimiters: ["[[", "]]"],

        /*todos meus dados que seria O array JSON, temos 2 array*/
        data:{
            pizzas : [],
            pizzas_selecionadas:[],
            bebidas:[],
            bebida_selecionada:{max_bebidas:0},
            num_bebidas_selecionada:[],
            tamanhos:[],
            tamanho_selecionado: {max_sabores:0},
            num_sabores_selecionado: {},
            pedido: {},

            // tamanhos_selecionados:[], //jogar fora
            // qtd_sabores:[], //acho que tb vai fora
            // qtd_sabores_selecionados: [], //e esse tambem...S


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
            adicionar_pizza: function(pizzas){
                this.pizzas_selecionadas.push(pizzas);
            },

                  /*busca as pizzas na api*/
            busca_pizzas: function () {
              this.$http.get('/api/pizza/').then(dados => {
                  this.pizzas = dados.body;
             })
            },

            /*funcao que remove as pizzas da comanda.*/
            remover_pizza: function (pizzas) {
                this.pizzas_selecionadas = this.pizzas_selecionadas.filter(x => x.id != pizzas.id);
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
            adicionar_tamanhos: function (tamanho) {
                this.tamanhos_selecionados.push(tamanho);
                }
            },
            remover_tamanhos: function(tamanhos){
                this.tamanhos_selecionados = this.tamanhos_selecionados.filter(x => x.id != tamanhos.id);
            },
            busca_qtd_sabores: function () {

                this.$http.get('api/sabores_pizza/').then(dados=>{
                    this.qtd_sabores = dados.body;
                     console.log("to aqui");
                })
            },

    });
/*fecha modal*/
    $('#btn-fecha').on('click', function () {
        $('.modal').modal('hide');
    });