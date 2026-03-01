<template>
  <div
    class="search-panel"
    ref="panelRef"
    @pointerdown="onPointerDown"
    @pointermove="onPointerMove"
    @pointerup="onPointerUp"
    @pointercancel="onPointerUp"
  >
    <!-- Triangle -->
    <div class="triangle"></div>

    <div class="panel-header">
      <h3 class="panel-title">Search</h3>

      <button class="close-button" @click="$emit('close')">
        <font-awesome-icon :icon="faTimes" />
      </button>
    </div>

    <input
      ref="inputRef"
      v-model="searchQuery"
      type="text"
      class="search-input"
      placeholder="Search by title or author..."
    />

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
const panelRef = ref(null)

const isDragging = ref(false)
const startX = ref(0)
const currentX = ref(0)
const translateX = ref(0)

const DRAG_THRESHOLD = 120
let animationFrame = null


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

  return result.value.getAllBooks.filter(book =>
    book.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    book.author.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})


onMounted(() => {
  nextTick(() => inputRef.value?.focus())
  window.addEventListener("keydown", handleEsc)
})

onUnmounted(() => {
  window.removeEventListener("keydown", handleEsc)
  if (animationFrame) cancelAnimationFrame(animationFrame)
})

function handleEsc(e) {
  if (e.key === "Escape") emit('close')
}

function onPointerDown(e) {
  if (!panelRef.value) return

  isDragging.value = true
  startX.value = e.clientX
  panelRef.value.style.transition = "none"

  panelRef.value.setPointerCapture(e.pointerId)
}

function onPointerMove(e) {
  if (!isDragging.value || !panelRef.value) return

  currentX.value = e.clientX
  const diff = currentX.value - startX.value

  if (diff <= 0) return

  translateX.value = diff

  if (animationFrame) cancelAnimationFrame(animationFrame)

  animationFrame = requestAnimationFrame(() => {
    panelRef.value.style.transform = `translate3d(${diff}px, 0, 0)`
  })
}

function onPointerUp(e) {
  if (!isDragging.value || !panelRef.value) return

  isDragging.value = false
  panelRef.value.releasePointerCapture(e.pointerId)

  if (translateX.value > DRAG_THRESHOLD) {
    emit('close')
  } else {
    panelRef.value.style.transition = "transform 0.28s cubic-bezier(.22,.61,.36,1)"
    panelRef.value.style.transform = `translate3d(0px, 0, 0)`
  }

  translateX.value = 0
}

</script>


<style scoped>

/* Main panel */
.search-panel {
  position: fixed;
  top: 80px;
  right: 40px;
  width: 420px;
  max-height: 450px;
  background: white;
  border-radius: 8px;
  padding: 20px;
  z-index: 2000;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.25);
  overflow-y: auto;
  animation: dropdownFade 0.18s ease;

  touch-action: none;

  will-change: transform;
  transform: translate3d(0, 0, 0);
  backface-visibility: hidden;
}

/* Triangle pointer */
.triangle {
  position: absolute;
  top: -10px;
  right: 35px; /* adjust to center under icon */
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid white;
}

/* Header */
.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.panel-title {
  font-size: 18px;
  font-weight: 600;
  margin: 0;
}

/* Input */
.search-input {
  width: 100%;
  margin-top: 15px;
  padding: 10px 12px;
  border-radius: 6px;
  border: 1px solid #ddd;
  font-size: 16px;
  outline: none;
  transition: border 0.2s ease;
}

.search-input:focus {
  border-color: #C06C84;
}

/* Close */
.close-button {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
}

.close-button svg {
  color: #333;
}

.close-button:hover svg {
  color: #C06C84;
}

/* Separator */
.separator {
  width: 100%;
  height: 2px;
  background: #eee;
  margin: 15px 0;
}

/* Results */
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
  font-size: 15px;
  font-weight: bold;
  color: black;
  transition: transform 0.15s ease;
  cursor: pointer;
}

.results li:hover {
  transform: translateX(4px);
}

.author {
  font-weight: normal;
}

.no-results {
  color: teal;
  font-weight: bold;
}

/* Animation */
@keyframes dropdownFade {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>