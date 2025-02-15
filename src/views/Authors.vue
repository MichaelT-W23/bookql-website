<template>
  <div class="container">
    <h1 class="page-title">✍🏻 Explore Our Authors</h1>

    <p v-if="loading" class="loading-text">Loading authors...</p>

    <p v-if="error" class="error-text">Error loading authors: {{ error.message }}</p>

    <ul v-if="authors.length" class="author-list">
      <li v-for="author in authors" :key="author.id" class="author-item">
        <AuthorCard :name="author.name" :details="author" />
      </li>
    </ul>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useQuery } from '@vue/apollo-composable';
import gql from "graphql-tag";
import AuthorCard from '../components/AuthorCard.vue';

const GET_ALL_AUTHORS = gql`
  query {
    getAllAuthors {
      id
      name
      age
      nationality
      books {
        id
        title
        publicationYear
        genre
      }
    }
  }
`;

const { result, loading, error, refetch } = useQuery(GET_ALL_AUTHORS);

const authors = computed(() => result.value?.getAllAuthors || []);

onMounted(() => {
  refetch();
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

.loading-text {
  font-size: 16px;
  color: #7b7b7b;
}

.error-text {
  font-size: 16px;
  color: #d9534f;
}

.author-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  justify-content: center;
  padding: 0;
  list-style: none;
  max-width: 800px;
  width: 100%;
}

.author-item {
  display: flex;
  justify-content: center;
}
</style>
