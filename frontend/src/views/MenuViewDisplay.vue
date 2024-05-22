<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" class="text-center">
                <h1>Menu View Display</h1>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <MenuViewTable></MenuViewTable>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import { VContainer, VRow, VCol } from 'vuetify/lib/components'
    import MenuViewTable from '@/components/MenuViewTable.vue'

    export default {
		name: 'MenuViewDisplay',
		components: {
            VContainer,
            VRow,
            VCol,
            MenuViewTable
        },
        data() {
            return {
            }
        }
    }
</script>

<style scoped>

</style>