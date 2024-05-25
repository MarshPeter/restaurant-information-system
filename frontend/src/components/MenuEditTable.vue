<template>
    <v-table>
        <template v-slot:default>
            <thead>
                <tr>
                    <th class="text-left">Item ID</th>
                    <th class="text-left">Name</th>
                    <th class="text-left">Price</th>
                    <th class="text-left">Nutrition Info</th>
                    <th class="text-left">Currently on Menu?</th>
                    <th class="text-left"></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in menuItems" :key="item.id">
                    <td>{{ item.id }}</td>
                    <td>{{ item.name }}</td>
                    <td>{{ item.price }}</td>
                    <td>{{ item.nutritionInfo }}</td>
                    <td>{{ item.onMenu ? "Yes" : "No" }}</td>
                    <td>
                        <v-btn color="primary" @click="invertMenuStatus(item)">{{ item.onMenu ? "Remove" : "Add to Menu" }}</v-btn>
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
        async invertMenuStatus(item) {
            console.log(item);
            console.log(item.id);
            console.log(item.onMenu);

            let url;

            console.log(item.onMenu);
            item.onMenu ? url = "http://localhost:5000/api/menu/remove-item-from-active-menu"
                : url = "http://localhost:5000/api/menu/add-item-to-active-menu"

            console.log(url);
            await fetch(url, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    "menuItem": item.id
                })
            });

            this.getMenu();

        },
        getMenu() {
            const url = "http://localhost:5000/api/menu/get-menu"

            fetch(url)
                .then((data) => data.json())
                .then((json) => this.menuItems = json.menu);

        }
    },
    beforeMount() {
        this.getMenu();
    }
}
</script>

<style scoped></style>