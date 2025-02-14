<template>
  <div class="container">
    <h1 class="page-title">📚 Explore Our Books</h1>

    <p v-if="loading" class="loading-text">Loading books...</p>

    <p v-if="error" class="error-text">Error loading books: {{ error.message }}</p>

    <ul v-if="books.length" class="book-list">
      <li v-for="book in books" :key="book.id" class="book-item">
        <BookCard :title="book.title" :body="book" />
      </li>
    </ul>
  </div>
</template>


<script setup>
import { computed } from 'vue';
import { useQuery } from '@vue/apollo-composable';
import gql from "graphql-tag";
import BookCard from '../components/BookCard.vue';

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

const { result, loading, error } = useQuery(GET_ALL_BOOKS);

const books = computed(() => result.value?.getAllBooks || []);

</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.page-title {
  padding-top: 15px;
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
  text-align: center;
  position: relative;
  letter-spacing: 1px;
}

.page-title::after {
  content: "";
  display: block;
  width: 400px;
  height: 4px;
  background-color: #ff6b6b;
  margin: 8px auto 0;
  border-radius: 2px;
}

.loading-text {
  font-size: 16px;
  color: #666;
}

.error-text {
  font-size: 16px;
  color: #d9534f;
}

.book-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  justify-content: center;
  padding: 0;
  list-style: none;
  max-width: 800px; 
  width: 100%;
}

.book-item {
  display: flex;
  justify-content: center;
}
</style>
