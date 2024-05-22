<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" class="text-center">
				<h1>Kitchen Display</h1>
			</v-col>
		</v-row>
		<KitchenTable></KitchenTable>
	</v-container>
</template>

<script>
	import KitchenTable from '@/components/KitchenTable.vue';
    import { VContainer, VRow, VCol } from 'vuetify/lib/components'
	
    export default {
		name: 'KitchenDisplayView',
		components: {
			KitchenTable,
			VContainer,
			VRow,
			VCol
		},
        data() {
            return {
            }
        }
    }
</script>

<style scoped>

</style>