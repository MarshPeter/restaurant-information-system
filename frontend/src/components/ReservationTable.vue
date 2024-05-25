<template>
    <v-table>
        <thead>
            <tr>
                <th scope="col">Reservation ID</th>
                <th scope="col">Date</th>
                <th scope="col">Time</th>
                <th scope="col">Number of Guests</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="reservation in reservations" :key="reservation.id">
                <td>{{ reservation.id }}</td>
                <td>{{ reservation.reservationDate }}</td>
                <td>{{ reservation.reservationTime }}</td>
                <td>{{ reservation.attendees }}</td>
                <td>
                    <v-btn color="primary" @click="cancelReservation(reservation.id)">Cancel</v-btn>
                </td>
            </tr>
        </tbody>
    </v-table>
</template>

<script>
import { VTable, VBtn } from 'vuetify/lib/components/index.mjs'

export default {
    name: 'ReservationTable',
    components: {
        VTable,
        VBtn
    },
    data() {
        return {
            reservations: []
        }
    },
    methods: {
        cancelReservation(reservationId) {
            console.log(`Canceling reservation with ID: ${reservationId}`);
        },
        correctTimesForReservations()  {
            console.log(this.reservations);
            for (let i = 0; i < this.reservations.length; i++) {
                let time = this.reservations[i].reservationTime;

                this.reservations[i].reservationTime = time.slice(0, 2) + ":" + time.slice(3);
            }
        }
    },
    beforeMount() {
        let url = "http://localhost:5000/api/reservation/all";
        fetch(url)
            .then(data => data.json())
            .then(jsonData => this.reservations = jsonData.reservations)
            .then(() => this.correctTimesForReservations())
            .catch(err => console.log(err));

    }
}
</script>

<style scoped></style>