import Vue from 'vue';

import VueRouter, {createWebHistory, RoutesConfig, createRouter} from 'vue-router';
import Home from "@/components/Home.vue"


const routes: Array<RoutesConfig> = [
    {
        path: '/',
        name: 'Home',
        redirectTo: '/home',
        component: Home,
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
