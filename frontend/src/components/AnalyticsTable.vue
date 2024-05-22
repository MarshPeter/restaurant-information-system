<template>
    <v-table>
        <template v-slot:default>
        <thead>
            <tr>
            <th>Date</th>
            <th>Total Sales</th>
            <th>Total Orders</th>
            <th>Total Customers</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="data in analytics" :key="data.id">
            <td>{{ data.date }}</td>
            <td>{{ data.totalSales }}</td>
            <td>{{ data.totalOrders }}</td>
            <td>{{ data.totalCustomers }}</td>
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
                analytics: [
                    {id: 1, date: '2021-09-01', totalSales: 1000, totalOrders: 10, totalCustomers: 5},
                    {id: 2, date: '2021-09-02', totalSales: 2000, totalOrders: 20, totalCustomers: 10},
                    {id: 3, date: '2021-09-03', totalSales: 3000, totalOrders: 30, totalCustomers: 15},
                    {id: 4, date: '2021-09-04', totalSales: 4000, totalOrders: 40, totalCustomers: 20}
                ]   
            }
        }
    }
</script>

<style scoped>

</style>