<template>
  <div class="container">
    <h1 class="page-title">🧙🏻‍♂️ Genres - {{ selectedGenre }}</h1>

    <label for="genre-select" class="genre-label">Select Genre:</label>
    <select v-model="selectedGenre" id="genre-select" class="genre-select">
      <option value="All">All</option>
      <option v-for="genre in genres" :key="genre" :value="genre">
        {{ genre }}
      </option>
    </select>

    <p v-if="loading" class="loading-text">Loading books...</p>

    <p v-if="error" class="error-text">Error loading books: {{ error.message }}</p>

    <ul v-if="books.length" class="book-list">
      <li v-for="book in books" :key="book.id" class="book-item">
        <BookCard :title="book.title" :body="book" />
      </li>
    </ul>

    <p v-if="!books.length && !loading" class="no-books-text">No books available.</p>
  </div>
</template>


<script setup>
import { ref, computed, watch, onMounted } from 'vue';
import { useQuery } from '@vue/apollo-composable';
import gql from "graphql-tag";
import BookCard from '../components/BookCard.vue';

const GET_ALL_GENRES = gql`
  query {
    getAllGenres
  }
`;

const GET_BOOKS_BY_GENRE = gql`
  query GetBooksByGenre($genre: String!) {
    getBooksByGenre(genre: $genre) {
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


const { result: genreResult, refetch: refetchGenres } = useQuery(GET_ALL_GENRES);
const genres = computed(() => genreResult.value?.getAllGenres || []);


const selectedGenre = ref("All");

const { result: allBooksResult, loading, error, refetch: refetchAllBooks } = useQuery(GET_ALL_BOOKS);
const { result: genreBooksResult, refetch: refetchBooksByGenre } = useQuery(GET_BOOKS_BY_GENRE, { genre: selectedGenre });

const books = computed(() => {
  return selectedGenre.value === "All"
    ? allBooksResult.value?.getAllBooks || []
    : genreBooksResult.value?.getBooksByGenre || [];
});

watch(selectedGenre, async (newGenre) => {
  if (newGenre === "All") {
    await refetchAllBooks();
  } else {
    await refetchBooksByGenre({ genre: newGenre });
  }
});

onMounted(async () => {
  await refetchGenres();
  await refetchAllBooks();
});

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

.genre-label {
  font-weight: bold;
  margin-bottom: 10px;
}

.genre-select {
  padding: 5px;
  font-size: 16px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.loading-text {
  font-size: 16px;
  color: #7b7b7b;
}

.error-text {
  font-size: 16px;
  color: #d9534f;
}

.no-books-text {
  font-size: 16px;
  color: #777;
}

.book-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  padding: 0;
  list-style: none;
  max-width: 600px;
  width: 100%;
  margin: 0 auto;
  padding-bottom: 100px;
}

.book-item {
  width: 100%;
  display: flex;
  justify-content: center; 
}

</style>
