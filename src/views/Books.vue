<template>
  <div>
    <p class="page-title">Books</p>

    <!-- Show loading state -->
    <p v-if="loading">Loading books...</p>

    <!-- Show error state -->
    <p v-if="error">Error loading books: {{ error.message }}</p>

    <!-- Display books -->
    <ul v-if="books.length">
      <li v-for="book in books" :key="book.id" class="book-item">
        <h3>{{ book.title }}</h3>
        <p><strong>Publication Year:</strong> {{ book.publicationYear }}</p>
        <p><strong>Genre:</strong> {{ book.genre }}</p>
        <p><strong>Author:</strong> {{ book.author.name }} ({{ book.author.nationality }}, Age: {{ book.author.age }})</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useQuery } from '@vue/apollo-composable';
import gql from "graphql-tag";


// Define the GraphQL query
const GET_ALL_BOOKS = gql`
  query {
    getAllBooks {
      id
      title
      publicationYear
      genre
      author {
        id
        name
        age
        nationality
      }
    }
  }
`;

// Execute the query
const { result, loading, error } = useQuery(GET_ALL_BOOKS);

// Extract books from query result
const books = computed(() => result.value?.getAllBooks || []);
</script>


<style scoped>
.page-title {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 10px;
}

.book-item {
  background: #f5f5f5;
  padding: 10px;
  margin: 10px 0;
  border-radius: 5px;
}
</style>
