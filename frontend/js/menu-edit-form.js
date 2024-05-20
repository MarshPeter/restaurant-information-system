app.component('menu-edit-form', {
    data() {
        return {
            menuItem: {
                name: '',
                category: '',
                price: 0
            },
            categories: ['Main Course', 'Side Dish', 'Drinks']
        }
    },
    methods: {
        createMenuItem() {
            // Logic to create the menu item
        }
    },
    template:
    `
    <div class="row">
        <div class="col">
            <h2>Create Menu Item</h2>
            <form @submit.prevent="createMenuItem">
                <div class="row">
                    <div class="col-md-6">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input type="text" id="name" v-model="menuItem.name" required class="form-control">
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="mb-3">
                            <label for="category" class="form-label">Category</label>
                            <select id="category" v-model="menuItem.category" required class="form-select">
                                <option v-for="category in categories" :key="category">{{ category }}</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <div class="mb-3">
                            <label for="price" class="form-label">Price</label>
                            <input type="number" id="price" v-model="menuItem.price" required class="form-control">
                        </div>
                    </div>
                    <div class="col-md-6">
                        <button type="submit" class="btn btn-primary">Create</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
    `
})
