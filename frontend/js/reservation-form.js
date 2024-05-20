app.component('reservation-form', {
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
    template:
    `
    <div class="row">
        <div class="col">
            <h2>Create Reservation</h2>
            <form @submit.prevent="createReservation">
            <div class="row">
                <div class="col-md-6">
                    <div class="mb-3">
                        <label for="table" class="form-label">Table</label>
                        <input type="text" class="form-control" id="table" v-model="table" required>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="mb-3">
                        <label for="date" class="form-label">Date</label>
                        <input type="date" class="form-control" id="date" v-model="date" required>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <div class="mb-3">
                        <label for="time" class="form-label">Time</label>
                        <input type="time" class="form-control" id="time" v-model="time" required>
                    </div>
                </div>
                <div class="col-md-6">
                <div class="mb-3">
                    <label for="guests" class="form-label">Number of Guests</label>
                    <input type="number" class="form-control" id="guests" v-model="guests" required>
                </div>
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Create Reservation</button>
            </form>
        </div>
    </div>
    `
})