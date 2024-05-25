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
                                id="nutrition"
                                label="Nutrition"
                                v-model="menuItem.nutrition"
                                :items="nutritionCategories"
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
                            <v-text-field
                                id="description"
                                label="Description"
                                v-model="menuItem.description"
                                required
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
                nutrition: '',
                price: 0,
                description: '',
            },
            nutritionCategories: ["", "Vegetarian", "Vegan", "Includes nuts"]
        }
    },
    methods: {
        async createMenuItem() {
            if (!this.validation()) {
                // TODO: IMPLEMENT Error handling I guess
                return;
            }

            const url = "http://localhost:5000/api/menu/create-item"

            await fetch(url, {
                method: "POST",
                headers: {
                    'Content-Type': "application/json"
                },
                body: JSON.stringify({
                    name: this.menuItem.name,
                    description: this.menuItem.description,
                    price: this.menuItem.price,
                    nutritionInfo: this.menuItem.nutrition
                })
            });

            this.$router.go();
        },
        validation() {
            // TODO: IMPLEMENT THESE EVENTUALLY IF TIME
            return true;
        },
        validateName() {

        },
        validateNutrition() {

        },
        validatePrice() {

        },
    },
}
</script>

<style scoped>

</style>