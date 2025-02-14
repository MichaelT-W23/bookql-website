<template>
  <div class="book-card">
    <div class="book-title-container">
      <h3 class="book-title">{{ title }}</h3>
    </div>
    <div class="book-details">
      <p><strong>Author:</strong> {{ body.author.name }} </p>
      <p><strong>Publication Year:</strong> {{ body.publicationYear }}</p>
      <p><strong>Genre:</strong> {{ body.genre }}</p>
    </div>
  </div>
</template>


<script setup>

defineProps({
  title: String,
  body: Object
});

</script>


<style scoped>
.book-card {
  width: 280px;
  background: #f8f9fa;
  border-radius: 12px;
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  cursor: pointer;
}

.book-card:hover {
  transform: translateY(-5px);
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.25);
}

.book-title-container {
  background: #6CC0A0;
  padding: 12px;
}

.book-title {
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  color: #fff;
  margin: 0;
}

.book-details {
  padding: 16px;
}

.book-details p {
  font-size: 14px;
  color: #555;
  margin-bottom: 6px;
}

.book-details p strong {
  color: #222;
}

</style>
