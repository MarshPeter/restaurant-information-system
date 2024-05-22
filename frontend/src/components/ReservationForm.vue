<template>
    <v-container>
        <v-row>
            <v-col>
                <h2>Create Reservation</h2>
                <v-form @submit.prevent="createReservation">
                    <v-row>
                        <v-col lg="4">
                            <v-text-field label="Table" v-model="table" required></v-text-field>
                        </v-col>
                        <v-col md="4">
                            <v-text-field label="Number of Guests" v-model="guests" type="number" required></v-text-field>
                        </v-col>
                        <v-col md="2">
                            <v-text-field label="Date" v-model="date" type="date" required></v-text-field>
                        </v-col>
                        <v-col md="2">
                            <v-text-field label="Time" v-model="time" type="time" required></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-btn type="submit" color="primary">Create Reservation</v-btn>
                    </v-row>
                </v-form>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { VContainer, VRow, VCol, VForm, VTextField, VBtn } from 'vuetify/lib/components'

export default {
    name: 'ReservationForm',
    components: {
        VContainer,
        VRow,
        VCol,
        VForm,
        VTextField,
        VBtn
    },
    data() {
        return {
            reservations: [],
            table: '',
            date: '',
            time: '',
            guests: ''
        }
    },
    methods: {
        createReservation() {
            this.reservations.push({
                id: this.reservations.length + 1,
                table: this.table,
                date: this.date,
                time: this.time,
                guests: this.guests,
                status: 'Pending'
            });
            this.table = '';
            this.date = '';
            this.time = '';
            this.guests = '';
        }
    },
}
</script>

<style scoped></style>