/*aqui criamos as estancias do vue*/



//---------------------------------------------------------------------------------
var app = new Vue({

    el: '#app',
    delimiters: ["[[", "]]"],

    /*todos meus dados que seria O array JSON, temos 2 array*/
    data: {
        tamanhos: [],
        sabores_pizza: [],
        sabores_borda: [],
        bebidas: [],
        formas_pagamento: [],


        tamanho_selecionado: {max_sabores: 0},
        num_sabores_selecionado: 0,
        sabores_selecionados: [],
        borda_selecionada: null,

        bebida_selecionada: null,
        opcao_bebida_selecionada:{},// {id: 0},
        //forma_pagamento_selecionada: null,

        num_bebidas_selecionada: 0, //retirar?

        pedido: {
            itens_pizza: [],
            itens_bebida: [],
            troco_para: 0,
            observacao: "",
            forma_de_pagamento: null,
            // total: 0,
            total: function () {
                total = 0;
                for (let i = 0; i < this.itens_pizza.length; i++) {
                    total += this.itens_pizza[i].preco();
                }
                for (let i = 0; i < this.itens_bebida.length; i++) {
                    total += this.itens_bebida[i].preco();
                }
                return total;
            },

            // cliente: 1 // TODO: remover essa linha... está provisória enquanto o sistema nao faz login
        },
        pedido_qt_erros: 0,
        pedido_erro_msg: "",


        cliente_data: {
            nome: "",
            telefone: "",
            endereco: {
                cep: "",
                logradouro: "",
                numero: "",
                complemento: "",
                bairro: "",
                cidade: "",
                uf: "",
            },
            usuario: {
                email: "",
                username: "",
                password: "",
                confirm_password: "",
            },
        },
        cliente_data_qt_errors: 0,
        cliente_data_errors: {
            nome: "",
            telefone: "",
            email: "",
            username: "",
            password: "",
            confirm_password: "",

            cep: "",
            logradouro: "",
            numero: "",
            complemento: "",
            bairro: "",
            cidade: "",
            uf: "",
        },


        login_data: {
            username: "",
            password: "",
        },
        jwt_token: null,
        // jwt_refresh_token: "",

        show_login_modal: false,
        is_logado :false,
        modal_login_mensagem : null,
        mensagem: null,

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
        this.is_logado = this.is_usuario_logado();
    },
    updated: function () {

    },
    watch: {
        tamanho_selecionado: function (event) {
            this.num_sabores_selecionado = 0;
        },
        'cliente_data.endereco.cep': function (newVal, oldVal) {
            if (newVal.replace("-", "").length === 8)
                this.preencher_endereco(newVal);
        },
    },
    methods: {
        seleciona_num_sabores(qtd) {
            this.num_sabores_selecionado = qtd;
            // console.log("qtd: "+qtd);
            this.sabores_selecionados = [];
            for (var i = 0; i < qtd; i++) {
                // console.log("i:"+i);
                // this.sabores_selecionados.push({"nome": ""});
                this.sabores_selecionados.push(null);
            }
        },
        adiciona_item_pizza() {
            let newItem_pizza = {
                tamanho_pizza: this.tamanho_selecionado,
                sabores: this.sabores_selecionados,
                sabor_borda: this.borda_selecionada,
                quantidade: 1,
                preco_un: parseFloat(this.tamanho_selecionado.preco) + parseFloat(this.borda_selecionada.valor_adicional),
                preco: function () {
                    return this.preco_un * this.quantidade;
                }
            }
            if (newItem_pizza.sabores.length > 0) { //se foi definido tamanho
                sabores_validos = 0;
                for (var i = 0; i < newItem_pizza.sabores.length; i++) {
                    if (newItem_pizza.sabores[i] != null)
                        sabores_validos++;
                }
                if (newItem_pizza.sabores.length === sabores_validos) { //se nenhum sabor for nulo
                    if (newItem_pizza.sabor_borda != null) { //se foi escolhida borda
                        adicional = 0;
                        for (var i = 0; i < newItem_pizza.sabores.length; i++) {
                            adicional += parseFloat(newItem_pizza.sabores[i].valor_adicional) + parseFloat(newItem_pizza.sabores[i].tipo_pizza.valor_adicional);
                        }
                        adicional = adicional / newItem_pizza.sabores.length;
                        newItem_pizza.preco_un = Math.round((newItem_pizza.preco_un + adicional) * 100) / 100;


                        //this.pedido.total += newItem_pizza.preco();
                        this.pedido.itens_pizza.push(newItem_pizza); //adiciona e limpa o cache
                        this.limpa_cache();
                    }

                }

            }
        },
        remove_item_pizza: function (index) {
            // this.pedido.itens_pizza = this.pedido.itens_pizza.filter(x => x.id != item.id);
            console.log("remove item index: " + index);
            // this.pedido.itens_pizza = this.pedido.itens_pizza.splice(index,1);
            //this.pedido.total -= this.pedido.itens_pizza[index].preco();
            this.pedido.itens_pizza.splice(index, 1);
        },
        adicionar_sabor_pizza: function (pizza) {
            if (this.sabores_selecionados.length < this.num_sabores_selecionado) {
                this.sabores_selecionados.push(pizza);
            }
        },
        adiciona_item_bebida: function () {
            if (this.bebida_selecionada != null) {
                if (this.opcao_bebida_selecionada != null) {
                    let newItemBebida = {
                        id: this.opcao_bebida_selecionada.id,
                        nome: this.bebida_selecionada.nome,
                        tamanho: this.opcao_bebida_selecionada.tamanho_bebida.nome,
                        quantidade: 1,
                        preco_un: Math.round(parseFloat(this.opcao_bebida_selecionada.preco) * 100) / 100,
                        preco: function () {
                            return this.preco_un * this.quantidade;
                        }
                    }//@@
                    //this.pedido.total += newItemBebida.preco();
                    this.pedido.itens_bebida.push(newItemBebida);
                    this.limpa_cache();
                }
            }
        },
        remove_item_bebida: function (index) {
            // this.pedido.itens_pizza = this.pedido.itens_pizza.filter(x => x.id != item.id);
            console.log("remove bebida item index: " + index);
            //this.pedido.total -= this.pedido.itens_bebida[index].preco();
            // this.pedido.itens_pizza = this.pedido.itens_pizza.splice(index,1);
            this.pedido.itens_bebida.splice(index, 1);
        },


        /*busca as pizzas na api*/
        busca_pizzas: function () {
            this.$http.get('/api/sabor_pizza/').then(dados => {
                this.sabores_pizza = dados.body;
            })
        },
        //
        // /*funcao que remove as pizzas da comanda.*/
        // remover_pizza: function (pizzas) {
        //     this.sabores_selecionados = this.sabores_selecionados.filter(x => x.id != pizzas.id);
        // },

        //Busca bebidas na API
        busca_bebidas: function () {
            this.$http.get('/api/bebida/').then(dados => {
                this.bebidas = dados.body;
            })
        },
        /*recebe o obj e add na lista*/
        // adicionar_bebidas: function (bebidas) {
        //     this.bebidas_selecionadas.push(bebidas);
        // },
        //
        // /*funcao que remove as pizzas da comanda.*/
        // remover_bebidas: function (bebidas) {
        //     this.bebidas_selecionadas = this.bebidas_selecionadas.filter(x => x.id != bebidas.id);
        // },

        busca_tamanhos: function () {
            this.$http.get('/api/tamanho_pizza/').then(dados => {
                this.tamanhos = dados.body;
            })
        },
        // adicionar_tamanhos: function (tamanho) {
        //     this.tamanhos_selecionados.push(tamanho);
        // },
        // remover_tamanhos: function (tamanhos) {
        //     this.tamanhos_selecionados = this.tamanhos_selecionados.filter(x => x.id != tamanhos.id);
        // },
        // busca_qtd_sabores: function () {
        //
        //     this.$http.get('api/sabores_pizza/').then(dados => {
        //         this.qtd_sabores = dados.body;
        //         console.log("to aqui");
        //     })
        // },
        busca_bordas: function () {
            this.$http.get('/api/sabor_borda/').then(dados => {
                this.sabores_borda = dados.body;
            })
        },
        busca_formas_pagamento: function () {
            this.$http.get('/api/forma_de_pagamento/').then(dados => {
                this.formas_pagamento = dados.body;
            })
        },
        enviar_pedido: function () {//@@
            this.validar_pedido();
            if (this.pedido_qt_erros == 0) {
                if (this.is_usuario_logado()) {
                    // this.show_login_modal = true;

                    let headers = {
                        'Content-Type': 'application/json',
                        "X-CSRFToken": token,
                        'Authorization': 'Bearer ' + this.jwt_token.access
                    };

                    this.$http.post(`/api/envio_pedido/`, this.pedido, {headers})
                        .then(response => {
                            // this.mensagemSucesso = `Solicitação ${this.escalaConfirma.id} ${aceita} com sucesso`;
                            if (response.status == 200) {
                                this.mensagem = "PEDIDO ENVIADO COM SUCESSO!"
                                //$('#mensagem').alert();
                            } else {
                                this.modal_login_mensagem = "Usuário/Senha incorreto(s)";
                            }

                        }).catch(erro => {

                    }).finally(() => {

                    });
                } else {
                    $('#modalLogin').modal('show');
                }
            }
        },

        limpa_cache: function () {
            this.tamanho_selecionado = {max_sabores: 0};
            this.num_sabores_selecionado = 0;
            this.sabores_selecionados = [];
            this.borda_selecionada = null;

            this.bebida_selecionada = null;
            this.opcao_bebida_selecionada = null;
        },

        preco_formatado: function (preco) {
            return preco.toLocaleString('pt-BR', {maximumFractionDigits: 2, style: 'currency', currency: 'BRL'});
        },

        is_usuario_logado: function () {
            this.jwt_token = JSON.parse(localStorage.getItem('jwt_token'));
            return this.jwt_token != null;
        },

        efetuar_login: function () {
            if (!this.is_usuario_logado()) {
                this.show_login_modal = true;
            }

            let headers = {
                'Content-Type': 'application/json',
                "X-CSRFToken": token
            };

            this.$http.post(`/api/token/`, this.login_data, {headers})
                .then(response => {
                    // this.mensagemSucesso = `Solicitação ${this.escalaConfirma.id} ${aceita} com sucesso`;
                    // console.log(response);
                    console.log(response.status)
                    if (response.status == 200) {
                        localStorage.setItem('jwt_token', JSON.stringify(response.data));
                        this.is_logado = true;
                        $('#modalLogin').modal('hide');
                    } else {
                        this.modal_login_mensagem = "Usuário/Senha incorreto(s)";
                    }

                }).catch(erro => {
                // console.log(erro);
                this.modal_login_mensagem = "Usuário/Senha incorreto(s)";

            }).finally(() => {

            });
        },
        efetuar_logout: function () {
            localStorage.removeItem('jwt_token');
            this.is_logado = false;
        },
        preencher_endereco: function (cep) {
            url = 'https://viacep.com.br/ws/' + cep + '/json/';
            this.$http.get(url).then(dados => {
                viacep = dados.body;

                this.cliente_data.endereco.logradouro = viacep.logradouro;
                this.cliente_data.endereco.complemento = viacep.complemento;
                this.cliente_data.endereco.bairro = viacep.bairro;
                this.cliente_data.endereco.cidade = viacep.localidade;
                this.cliente_data.endereco.uf = viacep.uf;
            })

        },
        validar_pedido: function () {
            this.pedido_qt_erros = 0;
            this.pedido_erro_msg = "";

            if (this.pedido.itens_pizza.length < 1) {
                this.pedido_qt_erros++;
                this.pedido_erro_msg = "Você não pediu nenhuma pizza!";
            } else if (this.pedido.forma_de_pagamento == null) {
                this.pedido_qt_erros++;
                this.pedido_erro_msg = "Você não escolheu forma de pagamento!";
            } else if (this.pedido.forma_de_pagamento.id == 1) {
                if (this.pedido.troco_para < this.pedido.total()) {
                    this.pedido_qt_erros++;
                    this.pedido_erro_msg = "Campo 'Troco Para' deve ser maior que o total...";
                }
            }

        },
        validar_cadastro: function () {

            this.cliente_data_errors.nome = "";
            this.cliente_data_errors.telefone = "";
            this.cliente_data_errors.email = "";
            this.cliente_data_errors.username = "";
            this.cliente_data_errors.password = "";
            this.cliente_data_errors.confirm_password = "";

            this.cliente_data_errors.cep = "";
            this.cliente_data_errors.logradouro = "";
            this.cliente_data_errors.numero = "";
            this.cliente_data_errors.complemento = "";
            this.cliente_data_errors.bairro = "";
            this.cliente_data_errors.cidade = "";
            this.cliente_data_errors.uf = "";

            this.cliente_data_qt_errors = 0;
            if (this.cliente_data.nome === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.nome = "Campo obrigatório"
            }
            if (this.cliente_data.telefone === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.telefone = "Campo obrigatório"
            }
            if (this.cliente_data.usuario.email === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.email = "Campo obrigatório"
            }
            if (this.cliente_data.usuario.username === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.username = "Campo obrigatório"
            }
            if (this.cliente_data.usuario.password === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.password = "Campo obrigatório"
            }
            if (this.cliente_data.usuario.password === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.password = "Campo obrigatório"
            } else if (this.cliente_data.usuario.password.length < 8) {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.password = "Senha deve possuir pelo menos 8 caracteres"
            }
            if (this.cliente_data.usuario.confirm_password !== this.cliente_data.usuario.password) {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.confirm_password = "Senhas devem coincidir"
            }
            //-----
            if (this.cliente_data.endereco.cep === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.cep = "Campo obrigatório"
            }
            if (this.cliente_data.endereco.logradouro === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.logradouro = "Campo obrigatório"
            }
            if (this.cliente_data.endereco.numero === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.numero = "Campo obrigatório"
            }
            if (this.cliente_data.endereco.bairro === "") {
                this.cliente_data_qt_errors++;
                this.cliente_data_errors.bairro = "Campo obrigatório"
            }
        },
        efetuar_cadastro_cliente: function () {
            this.validar_cadastro();
            if (this.cliente_data_qt_errors == 0) { //Formulário OK, pode enviar solicitacao de cadastro

                let headers = {
                    'Content-Type': 'application/json',
                    "X-CSRFToken": token
                };

                this.$http.post(`/api/cadastro_cliente/`, this.cliente_data, {headers})
                    .then(response => {
                        // this.mensagemSucesso = `Solicitação ${this.escalaConfirma.id} ${aceita} com sucesso`;
                        // console.log(response);
                        console.log(response.status)
                        if (response.status === 200) {

                            // localStorage.setItem('jwt_token', JSON.stringify(response.data));
                            // $('#modalCadastro').modal('hide');
                            $('#modalCadastro').modal('hide');
                        } else {
                            this.modal_login_mensagem = "Usuário/Senha incorreto(s)";
                        }

                    }).catch(erro => {
                    // console.log(erro);
                    //     this.modal_login_mensagem = "Usuário/Senha incorreto(s)";

                }).finally(() => {

                });
            }
        },
    },
});
/*fecha modal*/
$('#btn-fecha').on('click', function () {
    $('.modal').modal('hide');
});