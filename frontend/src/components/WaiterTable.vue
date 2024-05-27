<template>
    <v-table>
        <thead>
            <tr>
                <th class="text-left">Order ID</th>
                <th class="text-left">Table</th>
                <th class="text-left">Items</th>
                <th class="text-left">Status</th>
                <th class="text-left">Complete Order</th>
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
                    <v-btn color="primary" @click="completeOrder(order)">Complete Order</v-btn>
                </td>
            </tr>
        </tbody>
    </v-table>
</template>

<script>
import { VTable, VBtn } from 'vuetify/lib/components';

export default {
    name: 'WaiterTable',
    components: {
        VTable,
        VBtn
    },
    data() {
        return {
            orders: []
        }
    },
    created() {
        this.fetchOrders();
    },
    methods: {
        async fetchOrders() {
            try {
                const response = await fetch('http://localhost:5000/api/waiter/observer');
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const data = await response.json();
                this.orders = data.updates;
            } catch (error) {
                console.error("There was an error fetching the orders:", error);
            }
        },
        async completeOrder(order) {
            try {
                const response = await fetch('http://localhost:5000/api/waiter/update-status', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ order_number: order.order_number })
                });
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const data = await response.json();
                console.log(data.success);
                this.fetchOrders(); // Fetch updated orders
            } catch (error) {
                console.error("There was an error completing the order:", error);
            }
        }
    }
}
</script>

<style scoped></style>
