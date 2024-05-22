<template>
    <v-row>
        <v-col cols="12">
            <v-table>
                <thead>
                    <tr>
                        <th scope="col">Item ID</th>
                        <th scope="col">Name</th>
                        <th scope="col">Price</th>
                        <th scope="col">Category</th>
                        <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in menuItems" :key="item.id">
                        <td>{{ item.id }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.price }}</td>
                        <td>{{ item.category }}</td>
                        <td>
                            <v-btn color="primary" @click="addToOrder(item)">Add to Order</v-btn>
                        </td>
                    </tr>
                </tbody>
            </v-table>
        </v-col>
    </v-row>
    <v-row>
        <v-col cols="6">
            <v-table>
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Price</th>
                        <th scope="col">Amount</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in itemsToOrder" :key="item.id">
                        <td>{{ item.name }}</td>
                        <td>{{ item.price }}</td>
                        <td>{{ item.amount }}</td>
                    </tr>
                </tbody>
            </v-table>
        </v-col>
        <v-col cols="6">
            <h3>Order Summary</h3>
            <v-row>
                <v-col cols="12">
                    <h4>Total Price: {{ calculateTotalPrice() }}</h4>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12">
                    <v-btn color="primary" @click="submitOrder">Submit Order</v-btn>
                </v-col>
            </v-row>
        </v-col>
    </v-row>
</template>

<script>
import { VRow, VCol, VTable, VBtn } from 'vuetify/lib/components/index.mjs'
export default {
    name: 'MenuViewTable',
    components: {
        VRow,
        VCol,
        VTable,
        VBtn
    },
    data() {
        return {
            itemsToOrder: [],
            menuItems: [
                { id: 1, name: 'Burger', price: 10, category: 'Main Course' },
                { id: 2, name: 'Fries', price: 5, category: 'Side Dish' },
                { id: 3, name: 'Coke', price: 3, category: 'Drinks' },
                { id: 4, name: 'Pizza', price: 12, category: 'Main Course' },
                { id: 5, name: 'Salad', price: 8, category: 'Side Dish' },
                { id: 6, name: 'Iced Tea', price: 4, category: 'Drinks' }
            ]
        }
    },
    methods: {
        addToOrder(item) {
            const existingItem = this.itemsToOrder.find(i => i.id === item.id);
            if (existingItem) {
                existingItem.amount++;
            } else {
                this.itemsToOrder.push({ ...item, amount: 1 });
            }
        },
        submitOrder() {
            // Logic to submit the order goes here
        },
        calculateTotalPrice() {
            return this.itemsToOrder.reduce((total, item) => total + (item.price * item.amount), 0);
        }
    },
}
</script>

<style scoped></style>