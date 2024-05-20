app.component('menu-edit-table', {
    data() {
        return {
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
        removeMenuItem(item) {
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
                            <button class="btn btn-primary" @click="removeMenuItem(item)">Remove</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    `
})
