<template>
	<v-app-bar app>
		<v-btn to="/" text>
			<v-img src="/koala.png" max-height="35" alt="Relaxing Koala System Logo"></v-img>
		</v-btn>
		<v-toolbar-title>Relaxing Koala System</v-toolbar-title>
		<v-btn v-for="route in routes" :key="route.name" :to="route.path" text>
			{{ route.name }}
		</v-btn>
	</v-app-bar>
</template>

<script>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { VAppBar, VToolbarTitle, VBtn, VImg } from 'vuetify/lib/components'

export default {
	name: 'AppBar',
	components: {
		VAppBar,
		VToolbarTitle,
		VBtn,
		VImg
	},
	setup() {
		const router = useRouter();
		const routes = computed(() => router.getRoutes().filter(route => route.name));

		return {
			routes,
		};
	},
};
</script>

<style scoped>
/* Add any styles specific to this component here */
</style>