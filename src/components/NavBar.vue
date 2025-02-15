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
    </div>
  </nav>
</template>


<script setup>
import { ref } from 'vue';

const links = ref([
  { name: 'Books 📚', path: '/' },
  { name: 'Authors ✍🏻', path: '/authors' },
  { name: 'Genres 🧙🏻‍♂️', path: '/genres' },
  { name: 'Add Book 📘', path: '/add-book' },
  { name: 'Add Author 🖋️', path: '/add-author' }
]);

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
}

.nav-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 20px;
}

.nav-link {
  padding: 12px 20px;
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

</style>
