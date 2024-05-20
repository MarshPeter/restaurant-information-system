app.component('kitchen-table', {
    data() {
        return {
            orders: [
                {id: 1, table: 'Table 1', items: 'Burger, Fries, Coke', status: 'Not Started'},
                {id: 2, table: 'Table 2', items: 'Pizza, Salad, Iced Tea', status: 'In Progress'},
                {id: 3, table: 'Table 3', items: 'Pasta, Garlic Bread, Lemonade', status: 'Cooked'},
                {id: 4, table: 'Table 4', items: 'Spaghetti, Cheesecake, Iced Coffee', status: 'Cooked'}
            ]
        }
    },
    methods: {
        updateStatus(order, newStatus) {
            order.status = newStatus;
        }
    },
    template:
    `
    <div class="row">
        <div class="col">
            <!-- table with completed orders to be served -->
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th scope="col">Order ID</th>
                        <th scope="col">Table</th>
                        <th scope="col">Items</th>
                        <th scope="col">Status</th>
                        <th scope="col">Change Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="order in orders">
                        <td>{{ order.id }}</td>
                        <td>{{ order.table }}</td>
                        <td>{{ order.items }}</td>
                        <td>{{ order.status }}</td>
                        <td>
                        <select class="form-select" v-model="order.status" @change="updateStatus(order, $event.target.value)">
                            <option value="Not Started">Not Started</option>
                            <option value="In Progress">In Progress</option>
                            <option value="Cooked">Cooked</option>
                        </select>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    `
})
