import { createRouter, createWebHistory } from 'vue-router';

import Books from '../views/Books.vue';
import Authors from '../views/Authors.vue';
import Genres from '../views/Genres.vue';
import AddBook from '../views/AddBook.vue';
import AddAuthor from '../views/AddAuthor.vue';

const routes = [
	{
		path: '/',
		component: Books
	},
	{
		path: '/authors',
		component: Authors
	},
	{
		path: '/genres',
		component: Genres
	},
	{
		path: '/add-book',
		component: AddBook
	},
	{
		path: '/add-author',
		component: AddAuthor
	}
]

const router = createRouter({
	history: createWebHistory('/'),
	routes
});

export default router;