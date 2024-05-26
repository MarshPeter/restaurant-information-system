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
                <td>{{ order.order_number }}</td>
                <td>{{ order.table }}</td>
                <td>
                    <ul>
                        <li v-for="item in order.menu_items" :key="item.itemID">{{ item.name }} ({{ item.quantity }})</li>
                    </ul>
                </td>
                <td>{{ order.state }}</td>
                <td>
                    <v-select :items="statuses" v-model="order.state" @change="updateStatus(order)"
                        variant="outlined" density="comfortable"></v-select>
                </td>
            </tr>
        </tbody>
    </v-table>
</template>

<script>
import { VTable, VSelect } from 'vuetify/lib/components';

export default {
    name: 'KitchenTable',
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
                const response = await fetch('http://localhost:5000/api/kitchen/display');
                const data = await response.json();
                this.orders = data.orders;
            } catch (error) {
                console.error("There was an error fetching the orders:", error);
            }
        },
        async updateStatus(order) {
            try {
                const response = await fetch('http://localhost:5000/api/kitchen/update-status', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ order_number: order.order_number })
                });
                if (response.ok) {
                    console.log("Order status updated successfully");
                } else {
                    console.error("There was an error updating the order status:", await response.text());
                }
            } catch (error) {
                console.error("There was an error updating the order status:", error);
            }
        }
    },
}
</script>

<style scoped></style>
