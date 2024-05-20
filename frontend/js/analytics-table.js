app.component('analytics-table', {
    data() {
        return {
            analytics: [
                {date: '2021-09-01', totalSales: 1000, totalOrders: 10, totalCustomers: 5},
                {date: '2021-09-02', totalSales: 2000, totalOrders: 20, totalCustomers: 10},
                {date: '2021-09-03', totalSales: 3000, totalOrders: 30, totalCustomers: 15},
                {date: '2021-09-04', totalSales: 4000, totalOrders: 40, totalCustomers: 20}
            ]
        }
    },
    template:
    `
    <div class="row">
        <div class="col">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th scope="col">Date</th>
                        <th scope="col">Total Sales</th>
                        <th scope="col">Total Orders</th>
                        <th scope="col">Total Customers</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="data in analytics">
                        <td>{{ data.date }}</td>
                        <td>{{ data.totalSales }}</td>
                        <td>{{ data.totalOrders }}</td>
                        <td>{{ data.totalCustomers }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    `
})


