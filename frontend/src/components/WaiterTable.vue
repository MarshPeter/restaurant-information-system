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
            <tr v-for="order in orders" :key="order.id">
                <td>{{ order.id }}</td>
                <td>{{ order.table }}</td>
                <td>{{ order.items }}</td>
                <td>{{ order.status }}</td>
                <td>
                    <v-select class="form-select" v-model="order.status"
                        @change="updateStatus(order, $event.target.value)"
                        :items="['Waiting for Server', 'In Progress', 'Completed']"
                        variant="outlined"
                        >
                    </v-select>
                </td>
            </tr>
        </tbody>
    </v-table>
</template>

<script>
import { VTable, VSelect } from 'vuetify/lib/components'

export default {
    name: 'WaiterTable',
    components: {
        VTable,
        VSelect
    },
    data() {
        return {
            orders: [
                { id: 1, table: 'Table 1', items: 'Burger, Fries, Coke', status: 'Waiting for Server' },
                { id: 2, table: 'Table 2', items: 'Pizza, Salad, Iced Tea', status: 'Completed' },
                { id: 3, table: 'Table 3', items: 'Pasta, Garlic Bread, Lemonade', status: 'Completed' },
                { id: 4, table: 'Table 4', items: 'Spaghetti, Cheesecake, Iced Coffee', status: 'Completed' }
            ]
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