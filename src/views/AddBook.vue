<template>
  <div class="container">
    <h1 class="page-title">📘 Add a New Book</h1>
    
    <form @submit.prevent="submitBook" class="book-form">
      <label>
        Title:
        <input v-model="title" type="text" required />
      </label>

      <label>
        Publication Year:
        <input v-model.number="publicationYear" type="number" required />
      </label>

      <label>
        Genre:
        <select v-model="selectedGenre" required>
          <option v-for="genre in reactiveGenres" :key="genre" :value="genre">
            {{ genre }}
          </option>
          <option value="new">➕ Add New Genre</option>
        </select>
      </label>

      <div v-if="selectedGenre === 'new'" class="new-genre-section">
        <input v-model="newGenre" placeholder="New Genre" required />
      </div>

      <label>
        Author:
        <select v-model="selectedAuthorId" required>
          <option v-for="author in authors" :key="author.id" :value="author.id">
            {{ author.name }}
          </option>
        </select>
      </label>

      <button type="submit" :disabled="!isValid">Add Book</button>
    </form>

    <p v-if="error" class="error-text">Error: {{ error.message }}</p>
  </div>
</template>


<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useQuery, useMutation } from '@vue/apollo-composable';
import gql from "graphql-tag";

const error = ref(null);


const GET_ALL_AUTHORS = gql`
  query {
    getAllAuthors {
      id
      name
    }
  }
`;

const GET_ALL_GENRES = gql`
  query {
    getAllGenres
  }
`;

const CREATE_BOOK = gql`
  mutation createBook($title: String!, $publicationYear: Int!, $genre: String!, $authorId: Int!) {
    createBook(title: $title, publicationYear: $publicationYear, genre: $genre, authorId: $authorId) {
      id
      title
    }
  }
`;

const { result: authorsResult, refetch: refetchAuthors } = useQuery(GET_ALL_AUTHORS, null, {
  onError(err) {
    error.value = err;
  }
});

const { result: genresResult } = useQuery(GET_ALL_GENRES, null, {
  onError(err) {
    error.value = err;
  }
});


const authors = computed(() => authorsResult.value?.getAllAuthors || []);
const reactiveGenres = ref([]);

watch(genresResult, (newGenres) => {
  if (newGenres?.getAllGenres) {
    reactiveGenres.value = [...newGenres.getAllGenres];
  }
}, { immediate: true });


const title = ref("");
const publicationYear = ref(null);
const selectedGenre = ref("");
const newGenre = ref("");
const selectedAuthorId = ref("");


const { mutate: createBook } = useMutation(CREATE_BOOK, {
  onError(err) {
    error.value = err;
  }
});

const isValid = computed(() => {
  return (
    title.value.trim() &&
    publicationYear.value &&
    (selectedGenre.value !== "new" || newGenre.value.trim()) &&
    selectedAuthorId.value
  );
});


const submitBook = async () => {
  if (!isValid.value) return;

  const genre = selectedGenre.value === "new" ? newGenre.value.trim() : selectedGenre.value;
  const authorId = selectedAuthorId.value;

  if (!genre) {
    alert("Genre cannot be empty.");
    return;
  }

  try {
    await createBook({
      title: title.value,
      publicationYear: publicationYear.value,
      genre: genre,
      authorId: authorId,
    });

    alert("Book added successfully!");

    if (selectedGenre.value === "new" && !reactiveGenres.value.includes(newGenre.value.trim())) {
      reactiveGenres.value.push(newGenre.value.trim());
    }

    title.value = "";
    publicationYear.value = null;
    selectedGenre.value = "";
    newGenre.value = "";
    selectedAuthorId.value = "";

    error.value = null; 
  } catch (err) {
    error.value = err;
  }
};

onMounted(() => {
  refetchAuthors();
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
}

.page-title::after {
  content: "";
  display: block;
  width: 300px;
  height: 4px;
  background-color: teal;
  margin: 8px auto 0;
  border-radius: 2px;
}

.book-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 300px;
}

label {
  font-size: 16px;
}

input, select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.new-genre-section {
  margin-top: 10px;
}

button {
  padding: 10px;
  background-color: #ff6b6b;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  font-size: 16px;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.error-text {
  font-size: 16px;
  color: #d9534f;
}
</style>