import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import './style.css'
import App from './App.vue'
import TicTacToe from './components/TicTacToe.vue';
import HangMan from './components/HangMan.vue';
import MainBody from './components/mainBody.vue';


const routes = [
    {
        path:'/',
        component : MainBody
    },
    {
        path:'/tictactoe',
        component : TicTacToe
    },
    {
        path:'/hangman',
        component : HangMan
    },
]

const router = createRouter({
    routes,
    history:createWebHistory()
})


createApp(App).use(router).mount('#app');
