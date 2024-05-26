<template>
    <v-container>
        <v-row>
            <v-col>
                <h2>Create Reservation</h2>
                <v-form @submit.prevent="createReservation">
                    <v-row>
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
            date: '',
            time: '',
            guests: ''
        }
    },
    methods: {
        createReservation() {
            console.log(this.date);
            console.log(this.time);
            console.log(this.guests);
            let [hours, minutes] = this.time.split(":");
            const modifiedTime = hours + minutes;

            const url = "http://localhost:5000/api/reservation/create";

            // TODO: Use return value to showcase that the reservation was successul, and to communicate the reservationID
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': "application/json",
                },
                body: JSON.stringify({
                    'reservationDate': this.date,
                    'resTime': modifiedTime,
                    'attendees': this.guests
                })
            })
            .then(data => data.json())
            .then(json => console.log(json));
                
        }
    },
}
</script>

<style scoped></style>