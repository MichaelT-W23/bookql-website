import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import apolloClient from './lib/apolloClient';
import { provideApolloClient } from '@vue/apollo-composable';

const app = createApp(App);

// Provide Apollo Client globally
provideApolloClient(apolloClient);

app.use(router).mount('#app');