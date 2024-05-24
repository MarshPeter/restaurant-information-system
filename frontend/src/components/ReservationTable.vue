<template>
    <v-table>
        <thead>
            <tr>
                <th scope="col">Reservation ID</th>
                <th scope="col">Table</th>
                <th scope="col">Date</th>
                <th scope="col">Time</th>
                <th scope="col">Number of Guests</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="reservation in reservations" :key="reservation.id">
                <td>{{ reservation.id }}</td>
                <td>{{ reservation.table }}</td>
                <td>{{ reservation.date }}</td>
                <td>{{ reservation.time }}</td>
                <td>{{ reservation.guests }}</td>
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
            reservations: [
                { id: 1, table: 'Table 1', date: '2021-10-01', time: '18:00', guests: 4 },
                { id: 2, table: 'Table 2', date: '2021-10-02', time: '19:00', guests: 2 },
                { id: 3, table: 'Table 3', date: '2021-10-03', time: '20:00', guests: 6 }
            ]
        }
    },
    methods: {
        cancelReservation(reservationId) {
            console.log(`Canceling reservation with ID: ${reservationId}`);
        }
    },
    async beforeMount() {
        console.log("Hello, this is working");
        let url = "http://localhost:5000/api/reservation/all";
        let result = await fetch(url);
        console.log(await result.json());
    }
}
</script>

<style scoped></style>