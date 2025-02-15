<template>
  <div class="container">
    <h1 class="page-title">🖋️ Add a New Author</h1>

    <form @submit.prevent="submitAuthor" class="author-form">
      <label>
        Name:
        <input v-model="name" type="text" required />
      </label>

      <label>
        Age:
        <input v-model.number="age" type="number" required />
      </label>
      <p v-if="ageError" class="error-text">{{ ageError }}</p>

      <label>
        Nationality:
        <input v-model="nationality" type="text" required />
      </label>

      <button type="submit" :disabled="!isValid">Add Author</button>
    </form>

    <p v-if="error" class="error-text">Error: {{ error.message }}</p>
  </div>
</template>


<script setup>
import { ref, computed } from 'vue';
import { useMutation } from '@vue/apollo-composable';
import gql from "graphql-tag";

const error = ref(null);

const CREATE_AUTHOR = gql`
  mutation createAuthor($name: String!, $age: Int!, $nationality: String!) {
    createAuthor(name: $name, age: $age, nationality: $nationality) {
      id
      name
      age
      nationality
    }
  }
`;

const name = ref("");
const age = ref(null);
const nationality = ref("");

const { mutate: createAuthor } = useMutation(CREATE_AUTHOR, {
  onError(err) {
    error.value = err;
  }
});

const ageError = computed(() => {
  if (age.value !== null && (age.value < 10 || age.value > 110)) {
    return "Age must be between 10 and 110.";
  }
  return "";
});

const isValid = computed(() => {
  return (
    name.value.trim() &&
    age.value !== null &&
    age.value >= 10 &&
    age.value <= 110 &&
    nationality.value.trim()
  );
});

const submitAuthor = async () => {
  if (!isValid.value) return;

  try {
    await createAuthor({
      name: name.value,
      age: age.value,
      nationality: nationality.value.trim(),
    });

    alert("Author added successfully!");

    name.value = "";
    age.value = null;
    nationality.value = "";
    error.value = null;
  } catch (err) {
    error.value = err;
  }
};

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

.author-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 300px;
}

label {
  font-size: 16px;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
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
