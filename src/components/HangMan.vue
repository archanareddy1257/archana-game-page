<template>
    <div>
        <header class="bg-white shadow">
            <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
                <h1 class="text-3xl font-bold tracking-tight text-gray-900">Hang Man</h1>
            </div>
        </header>
        <main>
            <div class="mx-auto max-w-7xl py-6 sm:px-6 lg:px-8">
                <h3>Game Canvas Here </h3>
                <!-- Select Level -->
                <h4 class="font-mono font-bold text-blue-600">COMING SOON</h4>
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

                }   
            }
        },
        methods:{
            getResponse(){
                const path = 'http://localhost:5000/hangman';
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
                const path = 'http://localhost:5000/hangman';
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

<style lang="scss" scoped>

</style>