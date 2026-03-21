<template>
  <div class="search-panel">
    <div class="panel-header">
      <h3 class="panel-title">Search</h3>

      <button
        class="close-button"
        @click="$emit('close')"
      >
        <font-awesome-icon :icon="faTimes" />
      </button>
    </div>

    <div class="input-wrapper">
      <input
        ref="inputRef"
        v-model="searchQuery"
        type="text"
        class="search-input"
        placeholder="Search by title or author..."
      />

      <button
        v-if="searchQuery"
        class="clear-button"
        @click="clearSearch"
      >
        <font-awesome-icon :icon="faTimes" />
      </button>
    </div>

    <div class="separator"></div>

    <div v-if="filteredBooks.length" class="results">
      <ul>
        <li v-for="book in filteredBooks" :key="book.uuid">
          <strong>📚 {{ book.title }}</strong>
          <br />
          <span class="author">
            by {{ book.author.name }} ({{ book.publicationYear }})
          </span>
        </li>
      </ul>
    </div>

    <p v-else-if="searchQuery" class="no-results">
      No results found.
    </p>
  </div>
</template>


<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

const emit = defineEmits(['close'])

const searchQuery = ref("")
const inputRef = ref(null)

const GET_ALL_BOOKS = gql`
  query {
    getAllBooks {
      uuid
      title
      publicationYear
      genre
      author {
        name
      }
    }
  }
`

const { result } = useQuery(GET_ALL_BOOKS)

const filteredBooks = computed(() => {
  if (!result.value || !searchQuery.value) return []

  const query = searchQuery.value.toLowerCase()

  return result.value.getAllBooks.filter(book =>
    book.title.toLowerCase().includes(query) ||
    book.author.name.toLowerCase().includes(query)
  )
})

onMounted(() => {
  nextTick(() => inputRef.value?.focus())
  window.addEventListener("keydown", handleEsc)
})

onUnmounted(() => {
  window.removeEventListener("keydown", handleEsc)
})

function handleEsc(e) {
  if (e.key === "Escape") {
    emit('close')
  }
}

function clearSearch() {
  searchQuery.value = ""
  inputRef.value?.focus()
}

</script>


<style scoped>

.search-panel {
  position: fixed;
  top: 100px;
  left: 50%;
  transform: translateX(-50%);
  
  width: 420px;
  max-height: calc(100vh - 140px);

  background: white;
  border-radius: 12px;
  padding: 20px;
  z-index: 2000;

  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.3);

  display: flex;
  flex-direction: column;

  overflow-y: auto;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.panel-title {
  font-size: 20px;
  font-weight: 600;
  margin: 0;
}

.input-wrapper {
  position: relative;
  width: 100%;
  margin-top: 15px;
}

.search-input {
  width: 100%;
  padding: 10px 40px 10px 12px;
  border-radius: 6px;
  border: 1px solid #ddd;
  font-size: 16px;
  outline: none;
  transition: border 0.2s ease;
}

.search-input:focus {
  border-color: #C06C84;
}

.clear-button {
  position: absolute;
  right: 10px;
  top: 50%;
  font-size: 17px;
  transform: translateY(-50%);

  background: none;
  border: none;
  cursor: pointer;

  display: flex;
  align-items: center;
  justify-content: center;

  width: 28px;
  height: 28px;
  border-radius: 50%;

  transition: all 0.2s ease;
}

.clear-button svg {
  color: #999;
  transition: color 0.2s ease;
}

/* .clear-button:hover svg {
  color: red; 
} */

.close-button {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;

  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;
  transition: all 0.2s ease;
}

.close-button svg {
  color: #333;
  transition: color 0.2s ease;
}

.close-button:hover {
  background: rgba(192, 108, 132, 0.15);
}

.close-button:hover svg {
  color: #C06C84;
}

.separator {
  width: 100%;
  height: 2px;
  background: #eee;
  margin: 15px 0;
}

.results {
  overflow-y: auto;
  max-height: 300px;
  padding-right: 5px;
}

.results ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.results li {
  background: #5FA8D3;
  padding: 12px;
  border-radius: 6px;
  margin-bottom: 8px;
  font-size: 16px;
  font-weight: bold;
  color: black;
  cursor: pointer;
}

.results li:hover {
  background: #4e95be;
}

.author {
  font-weight: normal;
}

.no-results {
  color: teal;
  font-weight: bold;
  font-size: 16px;
}

</style>