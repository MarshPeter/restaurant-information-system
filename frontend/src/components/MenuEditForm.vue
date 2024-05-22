<template>
        <v-row>
            <v-col>
                <h2>Create Menu Item</h2>
                <v-form @submit.prevent="createMenuItem">
                    <v-row>
                        <v-col md="6">
                            <v-text-field
                                id="name"
                                label="Name"
                                v-model="menuItem.name"
                                required
                            ></v-text-field>
                        </v-col>
                        <v-col md="6">
                            <v-select
                                id="category"
                                label="Category"
                                v-model="menuItem.category"
                                :items="categories"
                                required
                            ></v-select>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col md="6">
                            <v-text-field
                                id="price"
                                label="Price"
                                v-model="menuItem.price"
                                required
                                type="number"
                            ></v-text-field>
                        </v-col>
                        <v-col md="6">
                            <v-btn type="submit" color="primary">Create</v-btn>
                        </v-col>
                    </v-row>
                </v-form>
            </v-col>
        </v-row>
</template>

<script>
import { VRow, VCol, VForm, VTextField, VSelect, VBtn } from 'vuetify/lib/components'

export default {
    name: 'MenuEditForm',
    components: {
        VRow,
        VCol,
        VForm,
        VTextField,
        VSelect,
        VBtn
    },
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
}
</script>

<style scoped>

</style>