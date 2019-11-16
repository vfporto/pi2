import axios from 'axios'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'

Vue.use(Vuex);
Vue.use(VueAxios, axios);

//armazenamos o JWT (token) localStorage e tambem no state storage mutacoes (mutatios) muda e define o estado do token
//VUE x sera reiniciada toda vez que o user att a pagina

// let payload;
const store = new VueAxios({
    state: {
        jwt: localStorage.getItem('t'),
        endpoint: {
            obtainJWT: 'http://127.0.0.1/8000/auth/obtain_token/',
            refreshJWT: 'http://127.0.0.1/8000/auth/refresh_token'
        }
    },
    mutations: {
        updateToken(state, newToken) {
            localStorage.setItem('t', newToken);
            state.jwt = newToken;
        },
        removeToken(state) {
            localStorage.removeItem('t');
            state.jwt = null;
        }
    },

    actions: {
        obtainToken(username, password) {
            const payload = {
                username: username,
                password: password
            }
            axios.post(this.endpoints.obtainJWT, payload)
                .then((responseDisplay)=>{
                    this.commit('updateToken', responseDisplay.data.token);
                })
                .catch((error)=>{
                    console.log(error);
                })
        },
        refreshToken(){
            const payload = {
            token: this.state.jwt
        }

         axios.post(this.endpoints.obtainJWT, payload)
                .then((responseDisplay)=>{
                    this.commit('updateToken', responseDisplay.data.token);
                })
                .catch((error)=>{
                    console.log(error);
                })
    },
    inspectToken(){
            //mais codigo por aqui
        }
    },

    methods: {
        say: function autenticate() {
            console.log("oia eu aqui...");
            console.log('teste');
            const payload = {
                username: this.username,
                password: this.password
            }
        }
    }

})



//instancias VUE