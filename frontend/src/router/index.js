// index.js file in routes
import { createRouter, createWebHistory } from 'vue-router'

import AnalyticsDisplay from '../views/AnalyticsDisplay.vue'
import KitchenDisplay from '../views/KitchenDisplay.vue'
import MenuEditDisplay from '../views/MenuEditDisplay.vue'
import MenuViewDisplay from '../views/MenuViewDisplay.vue'
import ReservationDisplay from '../views/ReservationDisplay.vue'
import WaiterDisplay from '../views/WaiterDisplay.vue'


const routes = [
    {
        path: '/analytics',
        name: 'Analytics',
        component: AnalyticsDisplay
    },
    {
        path: '/kitchen',
        name: 'Kitchen',
        component: KitchenDisplay
    },
    {
        path: '/menu-edit',
        name: 'Menu Edit',
        component: MenuEditDisplay
    },
    {
        path: '/menu-view',
        name: 'Menu View',
        component: MenuViewDisplay
    },
    {
        path: '/reservation',
        name: 'Reservation',
        component: ReservationDisplay
    },
    {
        path: '/waiter',
        name: 'Waiter',
        component: WaiterDisplay
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router