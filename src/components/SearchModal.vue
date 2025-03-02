<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <button class="close-button" @click="$emit('close')">✖</button>
      <h2>Search</h2>
      <input
        v-model="searchQuery"
        type="text"
        class="search-input"
        placeholder="Search for books, authors..."
      />
      <button class="search-submit" @click="performSearch">Search</button>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';

// Define emitted event
defineEmits(['close']);

const searchQuery = ref('');

const performSearch = () => {
  console.log("Searching for:", searchQuery.value);
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  text-align: center;
  position: relative;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
}

.search-input {
  width: 100%;
  padding: 10px;
  margin-top: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.search-submit {
  margin-top: 10px;
  background: #C06C84;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 4px;
  width: 100%;
}

.search-submit:hover {
  background: #F4A261;
}
</style>
