<template>
  <div>
    <p class="page-title">Genres - {{ selectedGenre }}</p>

    <!-- Genre Selection Dropdown -->
    <label for="genre-select">Select Genre:</label>
    <select v-model="selectedGenre" id="genre-select">
      <option value="All">All</option>
      <option v-for="genre in genres" :key="genre" :value="genre">
        {{ genre }}
      </option>
    </select>

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

    <p v-if="!books.length && !loading">No books available.</p>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useQuery } from '@vue/apollo-composable';
import gql from "graphql-tag";

// GraphQL query to fetch all available genres
const GET_ALL_GENRES = gql`
  query {
    getAllGenres
  }
`;

// GraphQL query to fetch books by selected genre
const GET_BOOKS_BY_GENRE = gql`
  query GetBooksByGenre($genre: String!) {
    getBooksByGenre(genre: $genre) {
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

// GraphQL query to fetch all books
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

// Fetch genres from GraphQL API
const { result: genreResult } = useQuery(GET_ALL_GENRES);
const genres = computed(() => genreResult.value?.getAllGenres || []);

// Reactive variable for selected genre
const selectedGenre = ref("All");

// Fetch books based on selected genre
const { result: allBooksResult, loading, error, refetch: refetchAllBooks } = useQuery(GET_ALL_BOOKS);
const { result: genreBooksResult, refetch: refetchBooksByGenre } = useQuery(GET_BOOKS_BY_GENRE, { genre: selectedGenre });

// Extract books from query result
const books = computed(() => {
  return selectedGenre.value === "All"
    ? allBooksResult.value?.getAllBooks || []
    : genreBooksResult.value?.getBooksByGenre || [];
});

// Watch for genre selection changes and refetch books accordingly
watch(selectedGenre, async (newGenre) => {
  if (newGenre === "All") {
    await refetchAllBooks();
  } else {
    await refetchBooksByGenre({ genre: newGenre });
  }
});
</script>

<style scoped>
.page-title {
  color: red;
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 10px;
}

.book-item {
  background: #f9f9f9;
  padding: 10px;
  margin: 10px 0;
  border-radius: 5px;
  border: 1px solid #ddd;
}

label {
  font-weight: bold;
  margin-right: 5px;
}

select {
  padding: 5px;
  font-size: 16px;
  margin-bottom: 15px;
}
</style>
