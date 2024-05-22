<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" class="text-center">
                    <h1>Reservation Display</h1>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
            <ReservationTable></ReservationTable>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
            <ReservationForm></ReservationForm>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import { VContainer, VRow, VCol } from 'vuetify/lib/components'
    import ReservationTable from '@/components/ReservationTable.vue'
    import ReservationForm from '@/components/ReservationForm.vue'

    export default {
		name: 'ReservationDisplay',
		components: {
            VContainer,
            VRow,
            VCol,
            ReservationTable,
            ReservationForm
        },
        data() {
            return {
            }
        }
    }
</script>

<style scoped>

</style>
