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
            <tr v-for="order in orders" :key="order.order_number">
                <td>{{ order.order_number }}</td>
                <td>{{ order.table }}</td>
                <td>
                    <ul>
                        <li v-for="item in order.menu_items" :key="item.itemID">{{ item.name }} ({{ item.quantity }})</li>
                    </ul>
                </td>
                <td>{{ order.state }}</td>
                <td>
                    <v-select
                        v-model="order.state"
                        @change="updateStatus(order)"
                        :items="statuses"
                        variant="outlined"
                        density="comfortable"
                    ></v-select>
                </td>
            </tr>
        </tbody>
    </v-table>
</template>

<script>
import { VTable, VSelect } from 'vuetify/lib/components';

export default {
    name: 'WaiterTable',
    components: {
        VTable,
        VSelect
    },
    data() {
        return {
            orders: [],
            statuses: ['LOGGING', 'INQUEUE', 'PREPARING', 'READYTOSERVE', 'COMPLETE']
        }
    },
    created() {
        this.fetchOrders();
    },
    methods: {
        async fetchOrders() {
            try {
                const response = await fetch('http://localhost:5000/api/waiter/display');
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const data = await response.json();
                this.orders = data.orders;
            } catch (error) {
                console.error("There was an error fetching the orders:", error);
            }
        },
        async updateStatus(order) {
            try {
                const response = await fetch('http://localhost:5000/api/waiter/update-status', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ order_id: order.order_number })
                });
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                console.log("Order status updated successfully");
            } catch (error) {
                console.error("There was an error updating the order status:", error);
            }
        }
    }
}
</script>

<style scoped></style>
