<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" class="text-center">
                <h1>Analytics</h1>
            </v-col>
        </v-row>
        <v-row justify="center">
            <v-col cols="12">
                <AnalyticsTable></AnalyticsTable>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import AnalyticsTable from '@/components/AnalyticsTable.vue'
    import { VContainer, VRow, VCol } from 'vuetify/lib/components'

    export default {
        name: 'AnalyticsView',
        components: {
            AnalyticsTable,
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