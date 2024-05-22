<template>
	<v-app-bar app color="primary">
		<v-img
			src="/images/koala-white.png"
			max-height="64"
			max-width="64"
			contain
		></v-img>
		<v-toolbar-title>Restaurant App</v-toolbar-title>
		<v-btn
			v-for="route in routes"
			:key="route.name"
			:to="{ name: route.name }"
			text
		>{{ route.name }}</v-btn>
	</v-app-bar>
</template>

<script>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { VImg, VToolbarTitle, VBtn } from 'vuetify/lib/components';

export default {
	name: 'AppBar',
	components: {
		VImg,
		VToolbarTitle,
		VBtn, // Add the missing import for VBtn component
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