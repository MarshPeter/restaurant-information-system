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
                        <v-btn @click="checkValidAttendance">Check If Suitable Time</v-btn>
                    </v-row>
                    <v-row v-if="validAttendanceTime">
                        <v-alert
                            color="success"
                            icon="$success"
                            title="Valid Time and Day"
                            :text="getValidTimeText()"></v-alert>
                    </v-row>
                    <v-row v-if="!validAttendanceTime && invalidMessage">
                        <v-alert
                            color="error"
                            icon="$error"
                            title="Invalid Time and Day"
                            :text="invalidMessage"></v-alert>
                    </v-row>
                    <v-row v-if="successfulReservation">
                        <v-alert
                            color="success"
                            icon="$success"
                            title="Reservation Successful"
                            :text="returnedReservationId"></v-alert>
                    </v-row>
                    <v-row v-if="validAttendanceTime" >
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
            guests: '',
            validAttendanceTime: false,
            invalidMessage: "",
            successfulReservation: false,
            returnedReservationId: "",
        }
    },
    methods: {
        getModifiedTime() {
            let [hours, minutes] = this.time.split(":");
            return hours + minutes;
        },
        getValidTimeText() {
            return `The time period you chose at ${this.time} ${this.date} is valid. Click below to proceed`;
        },
        checkValidAttendance() {
            const url = `http://localhost:5000/api/reservation/${this.getModifiedTime()}/${this.guests}/${this.date}`;

            console.log(url)
            try {
                fetch(url, {
                    mode: "cors"
                })
                .then(data => data.json())
                .then(json => {
                    if (json["success"]) {
                        console.log("valid")
                        this.validAttendanceTime = true;
                        return
                    } 
                    if (json["nextAvailable"]) {
                        console.log("suggesting a new time")
                        this.validAttendanceTime = false;
                        this.invalidMessage = `That slot is not possible Recommended time is: ${json["nextAvailable"]}`
                        return 
                    }
                    if (json["fail"]) {
                        this.validAttendanceTime = false;
                        console.log("No vacancy at that time or after that time")
                        this.invalidMessage = `There are no reservations at that time or after. Try another day or an earlier time`
                        return
                    }

                })
                .catch(err => console.log(err))
            } catch (err) {
                console.log(err);
            }
        },
        createReservation() {
            const modifiedTime = this.getModifiedTime();

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
            .then(json => {
                this.date = ''
                this.time = '',
                this.guests = '',
                this.validAttendanceTime = false,
                this.invalidMessage = "",
                this.successfulReservation = true,
                this.returnedReservationId = `your reservation ID: ${json['reservationId']}`

            });
                
        }
    },
}
</script>

<style scoped></style>