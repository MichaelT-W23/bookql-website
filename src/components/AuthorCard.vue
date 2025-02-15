<template>
  <div class="author-card">
    <div class="author-info">
      <h3 class="author-name">{{ name }}</h3>
      <p><strong>Age:</strong> {{ details.age }}</p>
      <p><strong>Nationality:</strong> {{ details.nationality }}</p>
    </div>
    
    <button class="toggle-books" @click="toggleBooks">
      {{ showBooks ? 'Hide Books' : 'See Books' }}
    </button>

    <div v-if="showBooks">
      <ul v-if="details.books && details.books.length" class="book-list">
        <li v-for="book in details.books" :key="book.id" class="book-item">
          <strong>• {{ book.title }}</strong> ({{ book.publicationYear }}) - {{ book.genre }}
        </li>
      </ul>
      <p v-else class="no-books-message">No books were found for this author.</p>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue';

defineProps({
  name: String,
  details: Object
});

const showBooks = ref(false);

const toggleBooks = () => {
  showBooks.value = !showBooks.value;
};

</script>


<style scoped>
.author-card {
  width: 300px;
  background: #f0f0f0;
  border-radius: 12px;
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
  padding: 16px;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.author-card:hover {
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.25);
}

.author-name {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
}

.toggle-books {
  background: teal;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  margin-top: 10px;
}

.toggle-books:hover {
  background: #006565;
}

.book-list {
  margin-top: 10px;
  padding: 0;
  list-style: none;
}

.book-item {
  font-size: 14px;
  color: #444;
  padding: 5px 0;
}

.no-books-message {
  font-size: 14px;
  margin-top: 10px;
}
</style>
