<template>
    <div>
        <header class="bg-white shadow">
            <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
                <h1 class="text-3xl font-bold tracking-tight text-gray-900">Tic Tac Toe</h1>
            </div>
        </header>
        <main>
            <div class="mx-auto max-w-7xl py-6 sm:px-6 lg:px-8 ">
                <!-- <h3>{{data.message}}</h3> -->
                <div v-if="data.Game.message">
                    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                        <strong class="font-bold">Invalid Move!</strong>
                        <span class="block sm:inline"> {{data.Game.message}}</span>
                        <span class="absolute top-0 bottom-0 right-0 px-4 py-3">
                          <svg class="fill-current h-6 w-6 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><title>Close</title><path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/></svg>
                        </span>
                    </div>
                </div>
                <div v-if="data.Game.status != 'GameOver' ">
                    <div class="flex justify-center py-4">
                        <h3 class="font-semibold text-gray-800 text-xl"> Now its {{data.Game.turn}}'s Turn</h3>
                    </div>
                    <div class="flex flex-col items-center mb-8">
                        <div class="grid grid-cols-3 gap-1">
                            <div v-for="index in 9" :key="index" class="border border-sky-950 w-20 h-20 hover:bg-slate-600 hover:text-slate-200 flex items-center justify-center text-4xl cursor-pointer"
                            @click="inputRecived(index)">
                                <!-- <div v-if="data.Game.board[index] == 'X'"> <img src="./../assets/tictactoe/cross.png" alt="X" width="44" height="44"> </div> -->
                                <!-- <div v-else-if="data.Game.board[index] == 'O'"> <img src="./../assets/tictactoe/circle.png" alt="O" width="44" height="44">    </div> -->
                                <!-- <div v-else> X </div> -->
                                {{ data.Game.board[index] }}
                            </div>
                        </div>
                    </div>  
                    <div class="flex justify-center py-8">
                        <button @click="inputRecived(10)" class="py-2 px-6 bg-blue-600 rounded-md text-slate-100">Reset</button>
                    </div>   
                </div>
                <div v-else>
                    <div >
                        <h3 class="flex justify-center font-bold text-green-500 text-6xl"> 🎉 Congratulations 🎊 </h3>
                        <br>
                        <h3 class="flex justify-center items-center font-mono font-bold text-emerald-600 text-4xl">Player '{{data.Game.winner}}' Own</h3>
                    </div>
                    <div class="flex justify-center py-12">
                        <button @click="inputRecived(10)" class="py-2 px-6 bg-blue-600 rounded-md text-slate-100 ">Play Again</button>
                    </div>  
                </div>
                             
            </div>
        </main>
    </div>
</template>

<script>
import axios from "axios";
    export default {
        data() {
            return {
                data: 
                {
                    "message": "Python Response",
                    'Game' :{
                        'winner': "None", 
                        'status': 'NotStarted', 
                        'turn': 'X',
                        'board':{
                            1:'',
                            2:'',
                            3:'',
                            4:'',
                            5:'',
                            6:'',
                            7:'',
                            8:'',
                            9:''
                        }
                    }
                }
            }
        },
        methods:{
            getResponse(){
                const path = 'http://localhost:5000/tictactoe';
                axios.get(path)
                .then((response) =>{
                    console.log(response.data);
                    this.data = response.data;
                    
                })
                .catch((error) =>{
                    console.log(error);
                });
            },
            inputRecived(index){
                const path = 'http://localhost:5000/tictactoe';
                let responseToSend = {"index" : index};
                axios.post(path,responseToSend)
                .then((response) =>{
                    console.log(response.data);
                    this.data = response.data;
                })
                .catch((error) =>{
                    console.log(error);
                });
            }
        },
        created(){
            this.getResponse();
        }
    }
</script>

<style scoped>
.serv ul {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
  }
  
  .serv ul li {
    list-style: none;
    flex: 0 0 33.333333%;
  }
</style>