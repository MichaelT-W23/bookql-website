<template>
  <nav class="navbar">
    <div class="nav-container">
      <div class="nav-links">
        <router-link
          v-for="link in links"
          :key="link.path"
          :to="link.path"
          class="nav-link"
        >
          {{ link.name }}
        </router-link>
      </div>

      <button class="search-button" @click="openSearch">
        <font-awesome-icon icon="search" />
      </button>
    </div>
  </nav>

  <!-- Overlay -->
  <div
    v-if="showSearch"
    class="overlay"
    @click="closeSearch"
  ></div>

  <!-- Side View -->
  <transition name="slide">
    <SearchSideView
      v-if="showSearch"
      @close="closeSearch"
    />
  </transition>
</template>

<script setup>
import { ref } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'
import SearchSideView from './SearchSideView.vue'

library.add(faSearch)

const links = ref([
  { name: 'Books 📚', path: '/' },
  { name: 'Authors ✍🏻', path: '/authors' },
  { name: 'Genres 🧙🏻‍♂️', path: '/genres' },
  { name: 'Add Book 📘', path: '/add-book' },
  { name: 'Add Author 🖋️', path: '/add-author' }
])

const showSearch = ref(false)

const openSearch = () => {
  showSearch.value = true
}

const closeSearch = () => {
  showSearch.value = false
}
</script>

<style scoped>
.navbar {
  background: #C06C84;
  width: 100%;
  position: fixed;
  height: 80px;
  top: 0;
  left: 0;
  z-index: 1000;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 20px;
}

.nav-link {
  padding: 12px 10px;
  font-size: 20px;
  font-weight: 600;
  color: #f1f1f1;
  text-decoration: none;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 1px;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.nav-link:hover {
  background: #F4A261;
}

.search-button {
  background: none;
  border: none;
  color: #f1f1f1;
  font-size: 21px;
  margin-left: 10px;
  cursor: pointer;
  padding: 10px;
  border-radius: 6px;
}

.search-button:hover {
  background-color: #F4A261;
}

.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  z-index: 900;
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}

.slide-enter-to,
.slide-leave-from {
  transform: translateX(0);
}
</style>
