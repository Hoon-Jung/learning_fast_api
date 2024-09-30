import { createStore } from 'vuex'
import persistedstate from 'vuex-persistedstate';


const store = createStore({
    plugins: [persistedstate()],
    state: {
        page: 0,
        access_token: "",
        username: "",
        is_login: false,
        store: "",
        keyword: "",
        commentPage: 0,
        sortby: "voter_count",
        desc: true,
    },
    mutations: {
        setPage: (state, payload) => state.page = payload ,
        setCommentPage: (state, payload) => state.commentPage = payload ,
        setAccessToken: (state, payload) => state.access_token = payload,
        setUsername: (state, payload) => state.username = payload,
        setIsLogin: (state, payload) => state.is_login = payload,
        setKeyword: (state, payload) => state.keyword = payload,
        setSortBy: (state, payload) => state.sortby = payload,
        setDesc: (state, payload) => state.desc = payload,
    },
    actions: {
        setPage: ({commit}, payload) => commit('setPage', payload),
        setCommentPage: ({commit}, payload) => commit('setCommentPage', payload),
        setAccessToken: ({commit}, payload) => commit('setAccessToken', payload),
        setUsername: ({commit}, payload) => commit('setUsername', payload),
        setIsLogin: ({commit}, payload) => commit('setIsLogin', payload),
        setKeyword: ({commit}, payload) => commit("setKeyword", payload),
        setSortBy: ({commit}, payload) => commit("setSortBy", payload),
        setDesc: ({commit}, payload) => commit("setDesc", payload),
    },
})

export default store