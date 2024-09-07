import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import(/* webpackChunkName: "about" */ '../views/HomeView.vue')
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "about" */ '../views/LoginView.vue')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import(/* webpackChunkName: "about" */ '../views/DashboardView.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/register',
    name: 'register',
    component: () => import(/* webpackChunkName: "about" */ '../views/RegisterView.vue')
  }
];

const router = createRouter({
  history: createWebHistory(), 
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const token = localStorage.getItem('access_token');
    if (!token) {
      next({ path: '/login' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
