<template>
    <v-table>
        <template v-slot:default>
            <thead>
                <tr>
                    <th class="text-left">Item ID</th>
                    <th class="text-left">Name</th>
                    <th class="text-left">Price</th>
                    <th class="text-left">Category</th>
                    <th class="text-left"></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in menuItems" :key="item.id">
                    <td>{{ item.id }}</td>
                    <td>{{ item.name }}</td>
                    <td>{{ item.price }}</td>
                    <td>{{ item.category }}</td>
                    <td>
                        <v-btn color="primary" @click="removeMenuItem(item)">Remove</v-btn>
                    </td>
                </tr>
            </tbody>
        </template>
    </v-table>
</template>

<script>
import { VTable, VBtn } from 'vuetify/lib/components'

export default {
    name: 'MenuEditTable',
    components: {
        VTable,
        VBtn
    },
    data() {
        return {
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
        removeMenuItem(item) {
            console.log(`Removing item: ${item.name}`);
        }
    },
    beforeMount() {
        const url = "http://localhost:5000/api/menu/get-menu"

        fetch(url)
            .then((data) => data.json())
            .then((json) => console.log(json));
    }
}
</script>

<style scoped></style>