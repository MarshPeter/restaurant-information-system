<template>
    <v-table>
        <template v-slot:default>
        <thead>
            <tr>
                <th>Food</th>
                <th>Monday</th>
                <th>Tuesday</th>
                <th>Wenesday</th>
                <th>Thursday</th>
                <th>Friday</th>
                <th>Saturday</th>
                <th>Sunday</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="data in test" :key="data.id">
                <td>{{ data["name"] }}</td>
                <td>{{ data.amounts.Monday }}</td>
                <td>{{ data.amounts.Tuesday }}</td>
                <td>{{ data.amounts.Wednesday }}</td>
                <td>{{ data.amounts.Thursday }}</td>
                <td>{{ data.amounts.Friday }}</td>
                <td>{{ data.amounts.Saturday }}</td>
                <td>{{ data.amounts.Sunday }}</td>
            </tr>
        </tbody>
        </template>
    </v-table>
</template>

<script>
    import { VTable } from 'vuetify/lib/components'
    export default {
        name: 'AnalyticsTable',
        components: {
            VTable
        },
        data() {
            return {
                analytics: []   
            }
        },
        methods: {
            getAllDailyAnalytics() {
                // const days = ['Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
                const tableResults = {}
                for (let item in this.analytics) {
                    if (!(item["Name"] in tableResults)) {
                        console.log(item["Name"]);
                        tableResults[item["Name"]] = [0, 0, 0, 0, 0, 0, 0];
                    }

                    let dayNumber = this.getNumberForDay(item.Day);
                    tableResults[item["Name"]][dayNumber] = item.Amount;
                }
                console.log(tableResults);
                return tableResults;
            },
            getNumberForDay(dayString) {
                const days = ['Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

                for (let i = 0; i < days.length; i++) {
                    if (days[i] === dayString) {
                        return i;
                    }
                }
            },
            getAnalytics() {
                const url = "http://localhost:5000/api/analytics";

                fetch(url)
                    .then(data => data.json())
                    .then(json => {
                        console.log(json);
                        this.analytics = json.analytics;
                        console.log(this.analytics);
                    })
            }
        },
        computed: {
            test() {
                return this.analytics.reduce((acc, obj) => {
                // Check if the name already exists in the accumulator
                if (!acc[obj.Name]) {
                    // If not, initialize an array for the name
                    acc[obj.Name] = {
                    name: obj.Name,
                    amounts: {
                        Monday: 0,
                        Tuesday: 0,
                        Wednesday: 0,
                        Thursday: 0,
                        Friday: 0,
                        Saturday: 0,
                        Sunday: 0
                    }
                    };
                }
                // Add the amount to the corresponding day of the week
                acc[obj.Name].amounts[obj.Day] += obj.Amount;
                return acc;
                }, {});
            }
        },
        created() {
            this.getAnalytics()
        }
    }
</script>

<style scoped>

</style>