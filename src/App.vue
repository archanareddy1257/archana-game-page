<template>
  <div>
    <MainNavBar/>
    <RouterView/>
    
  </div>

</template>

<script>

import TicTacToe from './components/TicTacToe.vue';
import MainBody from './components/mainBody.vue';
import MainNavBar from './components/mainNavBar.vue';

  export default {
    name: "Home",
    components: { MainBody, MainNavBar, TicTacToe },
    data() {
        return {

        };
    }
}
</script>

<style lang="scss" scoped>

</style>