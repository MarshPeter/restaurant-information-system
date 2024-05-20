app.component('reservation-table', {
    data() {
        return {
            reservations: [
                {id: 1, table: 'Table 1', date: '2021-10-01', time: '18:00', guests: 4},
                {id: 2, table: 'Table 2', date: '2021-10-02', time: '19:00', guests: 2},
                {id: 3, table: 'Table 3', date: '2021-10-03', time: '20:00', guests: 6}
            ]
        }
    },
    methods: {
        cancelReservation(reservationId) {
            // Logic to cancel the reservation
            // You can update the status of the reservation to 'Cancelled' or remove it from the reservations array
        }
    },
    template:
    `
    <div class="row">
        <div class="col">
            <!-- table of reservations -->
            <table class="table table-striped">
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
                    <tr v-for="reservation in reservations">
                        <td>{{ reservation.id }}</td>
                        <td>{{ reservation.table }}</td>
                        <td>{{ reservation.date }}</td>
                        <td>{{ reservation.time }}</td>
                        <td>{{ reservation.guests }}</td>
                        <td>
                            <button class="btn btn-danger" @click="cancelReservation(reservation.id)">Cancel</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    `
})
