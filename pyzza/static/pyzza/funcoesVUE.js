/*aqui criamos as estancias do vue*/



//---------------------------------------------------------------------------------
var app = new Vue({

    el: '#app',
    delimiters: ["[[", "]]"],

    /*todos meus dados que seria O array JSON, temos 2 array*/
    data: {
        // sabor_borda: {
        //     id: 1,
        //     nome: "",
        //     valor_adicional: 0
        // },
        //
        // item_pizza: {
        //     sabores: [],
        //     sabor_borda: {},
        //     tamanho_pizza: {},
        //     quantidade: 0,
        //     preco: 0,
        // },

        tamanhos: [],
        sabores_pizza: [],
        sabores_borda: [],
        bebidas: [],
        formas_pagamento: [],

        tamanho_selecionado: {max_sabores: 0},
        num_sabores_selecionado: 0,
        sabores_selecionados: [],
        borda_selecionada: {},

        bebida_selecionada: {},
        num_bebidas_selecionada: 0,
        pedido: {
            itens_pizza: [],
            itens_bebida: [],
            troco_para: 0,
            observacao: "",
            forma_de_pagamento: 1,
            cliente: 1
        }, //end pedido

    }, //end data

    /*quando gera a pagina, dentro temos uma funcao que sera executada quando a pagina for criada
    * podemos inserir todas as funcoes que quisermos executar qndo a pagina for criada.*/
    created: function () {
        this.busca_tamanhos();
        this.busca_pizzas();
        this.busca_bebidas();
        this.busca_bordas();
        this.busca_formas_pagamento();
    },
    mounted: function () {
        /*tudo que colocar aqui eh executado a pagina for montada*/
    },
    updated: function () {

    },
    watch: {
        tamanho_selecionado: function (event) {
            this.num_sabores_selecionado = 0;
        }
    },
    methods: {
        seleciona_num_sabores(qtd) {
            this.num_sabores_selecionado = qtd;
            // console.log("qtd: "+qtd);
            this.sabores_selecionados = [];
            for (var i = 0; i < qtd; i++) {
                // console.log("i:"+i);
                // this.sabores_selecionados.push({"nome": ""});
                this.sabores_selecionados.push({});
            }
        },
        adiciona_item_pizza() {
            let newItem_pizza = {
                tamanho_pizza: this.tamanho_selecionado,
                sabores: this.sabores_selecionados,
                sabor_borda: this.borda_selecionada,
                quantidade: 1,
                preco: 0,
            }
            this.pedido.itens_pizza.push(newItem_pizza);
            this.limpa_cache();

        },
        remove_item_pizza: function (index) {
            // this.pedido.itens_pizza = this.pedido.itens_pizza.filter(x => x.id != item.id);
            console.log("remove item index: "+index);
            // this.pedido.itens_pizza = this.pedido.itens_pizza.splice(index,1);
            this.pedido.itens_pizza.splice(index,1);
        },
        adicionar_sabor_pizza: function (pizza) {
            if (this.sabores_selecionados.length < this.num_sabores_selecionado) {
                this.sabores_selecionados.push(pizza);
            }
        },

        /*busca as pizzas na api*/
        busca_pizzas: function () {
            this.$http.get('/api/sabor_pizza/').then(dados => {
                this.sabores_pizza = dados.body;
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
        },
        remover_tamanhos: function (tamanhos) {
            this.tamanhos_selecionados = this.tamanhos_selecionados.filter(x => x.id != tamanhos.id);
        },
        busca_qtd_sabores: function () {

            this.$http.get('api/sabores_pizza/').then(dados => {
                this.qtd_sabores = dados.body;
                console.log("to aqui");
            })
        },
        busca_bordas: function () {
            this.$http.get('/api/sabor_borda/').then(dados => {
                this.sabores_borda = dados.body;
            })
        },
        busca_formas_pagamento: function () {
            this.$http.get('/api/sabor_borda/').then(dados => {
                this.sabores_borda = dados.body;
            })
        },
        limpa_cache: function () {
            this.tamanho_selecionado = {max_sabores: 0};
            this.num_sabores_selecionado = 0;
            this.sabores_selecionados = [];
            this.borda_selecionada = {};
        }

    },
});
/*fecha modal*/
$('#btn-fecha').on('click', function () {
    $('.modal').modal('hide');
});