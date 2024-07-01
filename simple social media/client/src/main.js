// import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';


import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import store from './store'

createApp(App).use(router).use(store).mount('#app')