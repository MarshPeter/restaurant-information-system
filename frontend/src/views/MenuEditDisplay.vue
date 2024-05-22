<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" class="text-center">
                    <h1>Menu Edit Display</h1>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
            <MenuEditTable></MenuEditTable>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <MenuEditForm></MenuEditForm>
            </v-col>
        </v-row>    
    </v-container>
</template>

<script>
    import { VContainer, VRow, VCol } from 'vuetify/lib/components'
    import MenuEditTable from '@/components/MenuEditTable.vue'
    import MenuEditForm from '@/components/MenuEditForm.vue'

    export default {
		name: 'MenuEditDisplay',
		components: {
            VContainer,
            VRow,
            VCol,
            MenuEditTable,
            MenuEditForm
        },
        data() {
            return {
            }
        }
    }
</script>

<style scoped>

</style>