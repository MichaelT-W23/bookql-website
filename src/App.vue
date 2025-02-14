<template>
	<NavBar></NavBar>

	<div class="main-view">
		<router-view />	
	</div>
</template>


<script setup>
import NavBar from './components/NavBar.vue';
</script>


<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

.main-view {
	padding-top: 80px;
}

</style>