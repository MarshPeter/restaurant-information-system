<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" class="text-center">
                <h1>Waiter Display</h1>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <WaiterTable></WaiterTable>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import { VContainer, VRow, VCol } from 'vuetify/lib/components'
    import WaiterTable from '@/components/WaiterTable.vue'
    export default {
		name: 'WaiterDisplay',
		components: {
            VContainer,
            VRow,
            VCol,
            WaiterTable
        },
        data() {
            return {
            }
        }
    }
</script>

<style scoped>

</style>