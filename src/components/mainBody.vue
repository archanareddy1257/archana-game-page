<template>

    <div class="bg-white">
        <div>
            <h1 class="flex justify-center mx-auto py-8 text-3xl font-bold text-gray-700 font-mono">👋  Welcome 2 Archana's Game Page 🛸</h1>
        </div>
      <div class="mx-auto max-w-2xl px-4 py-2 sm:px-6 sm:py-2 lg:max-w-7xl lg:px-8">
        <h2 class="text-2xl font-bold tracking-tight text-gray-900">LIST OF GAMES</h2>
  
        <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
          <div v-for="Game in Games" :key="Game.id" class="group relative">
            <div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80">
              <img :src="Game.image" :alt="Game.name" class="h-full w-full object-cover object-center lg:h-full lg:w-full" />
            </div>
            <div class="mt-4 flex justify-between">
              <div>
                <h3 class="text-sm text-gray-700">
                  <a :href="Game.href">
                    <span aria-hidden="true" class="absolute inset-0" />
                    {{ Game.name }}
                  </a>
                </h3>
                <p v-if="Game.Ready" class="mt-1 text-sm text-gray-500"> PLAY NOW </p>
                <p v-else class="mt-1 text-sm text-gray-500"> COMING SOON </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  

<script>
export default {
    name: "mainBody",
    data() {
        return {
            Games: [
                {
                    id: 1,
                    href: '/tictactoe',
                    name: "Tic Tac Toe",
                    image: "../../src/assets/tictactoe.jpg",
                    Ready: true
                },
                {
                    id: 2,
                    href: '/hangman',
                    name: "Hang Man",
                    image: "../../src/assets/hangman.jpg",
                    Ready: false
                }
            ]
        }
    },
}
</script>

<style lang="scss" scoped></style>