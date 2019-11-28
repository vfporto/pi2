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
            sabor_borda: {
                id: 1,
                nome: "",
                valor_adicional: 0
            },

            item_pizza:  {
                sabores: [ ],
                sabor_borda: {},
                tamanho_pizza: {},
                quantidade: 0,
                preco: 0,
            },

            pizzas : [],
            sabores_selecionados:[],
            bebidas:[],
            bebida_selecionada:{max_bebidas:0},
            num_bebidas_selecionada:[],
            tamanhos:[],
            tamanho_selecionado: {max_sabores:0},
            num_sabores_selecionado: 0,
            pedido:  {
                itens_pizza: [
                    //--------------------------
                    {
                        id: 1,
                        sabores: [
                            {
                                id: 1,
                                nome: "Calabresa",
                                descricao: "Pizza de calabresa c/ as melhores calabresas.",
                                valor_adicional: "0.00",
                                disponivel: true,
                                imagem: "http://127.0.0.1:8000/imagens/sabor_pizza_img/calabresa_tradicional_SkMrYjw.png",
                                tipo_pizza: 1
                            },
                            {
                                id: 3,
                                nome: "4 queijos",
                                descricao: "de 4 vaca diferente",
                                valor_adicional: "0.00",
                                disponivel: true,
                                imagem: "http://127.0.0.1:8000/imagens/sabor_pizza_img/4queijos_tradicional_RlRBepe.png",
                                tipo_pizza: 1
                            }
                        ],
                        sabor_borda: {
                            id: 1,
                            nome: "Catupiry",
                            valor_adicional: "3.00",
                            disponivel: true
                        },
                        tamanho_pizza: {
                            id: 2,
                            nome: "Média",
                            max_sabores: 1,
                            preco: "30.00",
                            multiplicador: "0.15",
                            ordem: 2,
                            disponivel: true
                        },
                        quantidade: 1,
                        preco: "0.00",
                        descontado_estoque: false,
                        pedido: 1
                    },
                    //------
                     {
                        id: 1,
                        sabores: [
                            {
                                id: 1,
                                nome: "Napolitana",
                                descricao: "Pizza de calabresa c/ as melhores calabresas.",
                                valor_adicional: "0.00",
                                disponivel: true,
                                imagem: "http://127.0.0.1:8000/imagens/sabor_pizza_img/calabresa_tradicional_SkMrYjw.png",
                                tipo_pizza: 1
                            },
                            {
                                id: 3,
                                nome: "Portuguesa",
                                descricao: "de 4 vaca diferente",
                                valor_adicional: "0.00",
                                disponivel: true,
                                imagem: "http://127.0.0.1:8000/imagens/sabor_pizza_img/4queijos_tradicional_RlRBepe.png",
                                tipo_pizza: 1
                            }
                        ],
                        sabor_borda: {
                            id: 1,
                            nome: "Sem Borda",
                            valor_adicional: "3.00",
                            disponivel: true
                        },
                        tamanho_pizza: {
                            id: 2,
                            nome: "Grande",
                            max_sabores: 1,
                            preco: "30.00",
                            multiplicador: "0.15",
                            ordem: 2,
                            disponivel: true
                        },
                        quantidade: 2,
                        preco: "0.00",
                        descontado_estoque: false,
                        pedido: 1
                    }
                    //------
                //--------------------
                ],
                itens_bebida: [],
                troco_para: 0,
                observacao: "",
                forma_de_pagamento: 1,
                cliente: 1
            },

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
            seleciona_num_sabores(qtd){
              this.num_sabores_selecionado = qtd;
            },
            adiciona_item_pizza(){
                ip = new this.item_pizza();
                this.pedido.itens_pizza.push(ip);
            },
            adicionar_sabor_pizza: function(pizza){
                if(this.sabores_selecionados.length < this.num_sabores_selecionado) {
                    this.sabores_selecionados.push(pizza);
                }
            },

                  /*busca as pizzas na api*/
            busca_pizzas: function () {
              this.$http.get('/api/pizza/').then(dados => {
                  this.pizzas = dados.body;
                  console.log(this.pizzas);
             })
            },

            /*funcao que remove as pizzas da comanda.*/
            remover_pizza: function (pizzas) {
                this.sabores_selecionados = this.sabores_selecionados.filter(x => x.id != pizzas.id);
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