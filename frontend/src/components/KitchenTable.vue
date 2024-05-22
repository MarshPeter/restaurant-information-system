<template>
    <v-table>
        <thead>
            <tr>
                <th class="text-left">Order ID</th>
                <th class="text-left">Table</th>
                <th class="text-left">Items</th>
                <th class="text-left">Status</th>
                <th class="text-left">Change Status</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(order, index) in orders" :key="index">
                <td>{{ order.id }}</td>
                <td>{{ order.table }}</td>
                <td>{{ order.items }}</td>
                <td>{{ order.status }}</td>
                <td>
                    <v-select :items="statuses" v-model="order.status" @change="updateStatus(order, $event)"
                        variant="outlined" density="comfortable"></v-select>
                </td>
            </tr>
        </tbody>
    </v-table>
</template>

<script>
import { VTable, VSelect } from 'vuetify/lib/components'

export default {
    name: 'KitchenTable',
    components: {
        VTable,
        VSelect
    },
    data() {
        return {
            orders: [
                { id: 1, table: 'Table 1', items: 'Burger, Fries, Coke', status: 'Not Started' },
                { id: 2, table: 'Table 2', items: 'Pizza, Salad, Iced Tea', status: 'In Progress' },
                { id: 3, table: 'Table 3', items: 'Pasta, Garlic Bread, Lemonade', status: 'Cooked' },
                { id: 4, table: 'Table 4', items: 'Spaghetti, Cheesecake, Iced Coffee', status: 'Cooked' }
            ],
            statuses: ['Not Started', 'In Progress', 'Cooked']
        }
    },
    methods: {
        updateStatus(order, newStatus) {
            order.status = newStatus;
        }
    },
}
</script>

<style scoped></style>