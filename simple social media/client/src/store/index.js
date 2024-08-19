import { createStore } from 'vuex'
import persistedstate from 'vuex-persistedstate';


const store = createStore({
    plugins: [persistedstate()],
    state: {
        page: 0,
        access_token: "",
        username: "",
        is_login: false,
<<<<<<< HEAD
=======
        store: "",
        keyword: "",
>>>>>>> e3febfa (added a couple features)
    },
    mutations: {
        setPage: (state, payload) => state.page = payload ,
        setAccessToken: (state, payload) => state.access_token = payload,
        setUsername: (state, payload) => state.username = payload,
        setIsLogin: (state, payload) => state.is_login = payload,
<<<<<<< HEAD
=======
        setKeyword: (state, payload) => state.keyword = payload,
>>>>>>> e3febfa (added a couple features)
    },
    actions: {
        setPage: ({commit}, payload) => commit('setPage', payload),
        setAccessToken: ({commit}, payload) => commit('setAccessToken', payload),
        setUsername: ({commit}, payload) => commit('setUsername', payload),
        setIsLogin: ({commit}, payload) => commit('setIsLogin', payload),
<<<<<<< HEAD
=======
        setKeyword: ({commit}, payload) => commit("setKeyword", payload),
>>>>>>> e3febfa (added a couple features)
    },
})

export default store