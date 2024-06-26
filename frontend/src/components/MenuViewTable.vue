<template>
    <v-row>
        <v-col cols="12">
            <v-table>
                <thead>
                    <tr>
                        <th scope="col">Item ID</th>
                        <th scope="col">Name</th>
                        <th scope="col">Price</th>
                        <th scope="col">Description</th>
                        <th scope="col">Nutrition Info</th>
                        <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in availableItems()" :key="item.id">
                        <td>{{ item.id }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.price }}</td>
                        <td>{{ item.description }}</td>
                        <td>{{ item.nutritionInfo }}</td>
                        <td>
                            <v-btn color="primary" @click="addToOrder(item)">Add to Order</v-btn>
                        </td>
                    </tr>
                </tbody>
            </v-table>
        </v-col>
    </v-row>
    <v-row v-if="orderCreated && validOrder">
        <v-alert
            color="success"
            icon="$success"
            title="Order Created!"
            text="Your order will be delivered as soon as possible"></v-alert>
    </v-row>
    <v-row v-if="orderCreated && !validOrder">
        <v-alert
            color="error"
            icon="error"
            title="Order Failed"
            :text="orderResponse"></v-alert>
    </v-row>
    <v-row>
        <v-col cols="6">
            <v-table>
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Price</th>
                        <th scope="col">Quantity</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in itemsToOrder" :key="item.id">
                        <td>{{ item.name }}</td>
                        <td>{{ item.price }}</td>
                        <td>{{ item.quantity}}</td>
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
                <v-col cols="12">
                    <label for="cname">Customer Name: </label>
                    <input type="text" id="cname" name="cname" v-model="customerName" >
                </v-col>
                <v-col cols="12">
                    <label for="table">Table Number:</label>
                    <input type="text" id="table" name="table" v-model="tableNumber" >
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
                { id: 1, name: 'Burger', price: 10, description: 'Main Course', menuStatus: 1 },
                { id: 2, name: 'Fries', price: 5, description: 'Side Dish', menuStatus: 1 },
                { id: 3, name: 'Coke', price: 3, description: 'Drinks', menuStatus: 1 },
                { id: 4, name: 'Pizza', price: 12, description: 'Main Course', menuStatus: 1 },
                { id: 5, name: 'Salad', price: 8, description: 'Side Dish', menuStatus: 1 },
                { id: 6, name: 'Iced Tea', price: 4, description: 'Drinks', menuStatus: 1 }
            ],
            customerName: "",
            tableNumber: "",
            orderCreated: false,
            validOrder: false,
            orderResponse: "",
        }
    },
    methods: {
        addToOrder(item) {
            const existingItem = this.itemsToOrder.find(i => i.id === item.id);
            if (existingItem) {
                existingItem.quantity++;
            } else {
                this.itemsToOrder.push({ ...item, quantity: 1 });
            }
        },
        submitOrder() {
            this.orderResponse = "";
            this.validateInputs();
            if (this.orderResponse !== "") {
                this.validOrder = false;
                this.orderCreated = true;
                return false;
            }
            let requestOptions = {
                method: "POST",
                mode: 'cors',
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    "customerName": this.customerName,
                    "totalCost": this.calculateTotalPrice(),
                    "table": this.tableNumber,
                    // Just going to set this to be inrestaurant only, we can change later if time allows - Peter
                    "orderType": "inRestaurant",
                    "menuItems": this.itemsToOrder
                })
            }
            fetch("http://localhost:5000/api/order/create", requestOptions)
                .then(data => data.json())
                .then(json => {
                    if (json['success']) {
                        this.orderResponse = json['success'];
                    }
                    this.itemsToOrder = [];
                    this.customerName = "";
                    this.tableNumber = "";
                    this.orderCreated = true;
                    this.validOrder = true;
                })
                .catch(err => console.log(err));
        },
        availableItems() {
            return this.menuItems.filter(item => item["onMenu"])
        },
        validateInputs() {
            // implement eventually if time allows, but who are we talking about, no chance there is time - Peter
            this.validateItems();
            this.validateName();
            this.validateTable();

        },
        validateItems() {
            if (this.itemsToOrder.length === 0) {
                this.orderResponse += "Must include menu items.";
            }
        },
        validateName() {
            const regex = /^[a-zA-Z\s]+$/;
            this.orderResponse = '';

            if (!regex.test(this.customerName)) {
                this.orderResponse += " Name may only contain alphabetical characters and spaces.";
            } 
        },
        validateTable() {
            if (this.tableNumber === "") {
                this.orderResponse += " Must include a table Number.";
            }
        },
        calculateTotalPrice() {
            return this.itemsToOrder.reduce((total, item) => total + (item.price * item.quantity), 0);
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
        console.log(this.menuItems);
    }
}
</script>

<style scoped></style>