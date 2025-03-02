<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <div class="modal-header">
        <input
          v-model="searchQuery"
          type="text"
          class="search-input"
          placeholder="Search by title or author..."
        />
        <button class="close-button" @click="$emit('close')">
          <font-awesome-icon :icon="faTimes" />
        </button>
      </div>
      <div class="separator"></div> 
      <div v-if="filteredBooks.length" class="results">
        <ul>
          <li v-for="book in limitedBooks" :key="book.id">
            <strong>{{ book.title }}</strong> by {{ book.author.name }} ({{ book.publicationYear }})
          </li>
        </ul>
      </div>
      <p v-else-if="searchPerformed">No results found.</p>
    </div>
  </div>
</template>


<script setup>
import { ref, computed } from 'vue';
import { useQuery } from '@vue/apollo-composable';
import gql from "graphql-tag";
import { faTimes } from '@fortawesome/free-solid-svg-icons';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faTimes);

defineEmits(['close']);

const searchQuery = ref("");
const searchPerformed = ref(false);

const GET_ALL_BOOKS = gql`
  query {
    getAllBooks {
      id
      title
      publicationYear
      genre
      author {
        name
      }
    }
  }
`;

const { result } = useQuery(GET_ALL_BOOKS);

const filteredBooks = computed(() => {
  if (!result.value || !searchQuery.value) return [];
  return result.value.getAllBooks.filter(book => 
    book.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    book.author.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const limitedBooks = computed(() => filteredBooks.value.slice(0, 5));

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
  border-radius: 12px;
  width: 450px; 
  height: 300px;
  text-align: center;
  position: relative;
  display: flex;
  flex-direction: column;
  font-size: 16px;
  padding: 15px;
  overflow: hidden;
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 10px;
}

.search-input {
  flex-grow: 1;
  padding: 6px;
  border: none;
  outline: none;
  font-size: 16px;
}

.close-button {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  margin-left: 10px;
}

.close-button svg {
  color: #333; 
}

.close-button:hover svg {
  color: #C06C84;
}

.separator {
  width: 100%;
  height: 1px;
  background: #ddd;
  margin: 0;
  flex-shrink: 0; 
}

.results {
  margin-top: 10px;
  text-align: left;
  max-height: 210px;
  overflow-y: auto;
}

.results ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.results li {
  background: #f9f9f9;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 4px;
  font-size: 16px;
}

</style>
