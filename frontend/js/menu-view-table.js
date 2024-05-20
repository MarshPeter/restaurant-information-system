app.component('menu-view-table', {
    data() {
        return {
            itemsToOrder: [],
            menuItems: [
                {id: 1, name: 'Burger', price: 10, category: 'Main Course'},
                {id: 2, name: 'Fries', price: 5, category: 'Side Dish'},
                {id: 3, name: 'Coke', price: 3, category: 'Drinks'},
                {id: 4, name: 'Pizza', price: 12, category: 'Main Course'},
                {id: 5, name: 'Salad', price: 8, category: 'Side Dish'},
                {id: 6, name: 'Iced Tea', price: 4, category: 'Drinks'}
            ]
        }
    },
    methods: {
        addToOrder(item) {
            const existingItem = this.itemsToOrder.find(i => i.id === item.id);
            if (existingItem) {
                existingItem.amount++;
            } else {
                this.itemsToOrder.push({...item, amount: 1});
            }
        },
        submitOrder() {
            // Logic to submit the order goes here
        },
        calculateTotalPrice() {
            return this.itemsToOrder.reduce((total, item) => total + (item.price * item.amount), 0);
        }
    },
    template:
    `
    <div class="row">
        <div class="col">
            <!-- table with menu items -->
            <table class="table table-striped">
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
                    <tr v-for="item in menuItems">
                        <td>{{ item.id }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.price }}</td>
                        <td>{{ item.category }}</td>
                        <td>
                            <button class="btn btn-primary" @click="addToOrder(item)">Add to Order</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="row">
        <div class="col-md-6">
            <!-- table with items to be ordered -->
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Price</th>
                        <th scope="col">Amount</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in itemsToOrder">
                        <td>{{ item.name }}</td>
                        <td>{{ item.price }}</td>
                        <td>{{ item.amount }}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="col-md-6">
            <h3>Order Summary</h3>
            <div class="row">
                <div class="col">
                    <h4>Total Price: {{ calculateTotalPrice() }}</h4>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <button class="btn btn-primary" @click="submitOrder">Submit Order</button>
                </div>
            </div>
        </div>
    </div>
    `
})
