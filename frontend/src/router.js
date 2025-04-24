import { createRouter, createWebHistory } from 'vue-router'
import RegisterForm from './components/RegisterForm.vue'
import LoginForm from './components/LoginForm.vue'
import ExpenseDashboard from './components/ExpenseDashboard.vue'
import Analytics from './components/Analytics.vue'


const routes = [
  { path: '/', redirect: '/login' },
  { path: '/register', component: RegisterForm },
  { path: '/login', component: LoginForm },
  {
    path: '/dashboard',
    component: ExpenseDashboard,
    meta: { requiresAuth: true }
    
  },
  { path: '/analytics', component: Analytics, meta: { requiresAuth: true } } // Add this line
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 🔐 Navigation guard
router.beforeEach((to, from, next) => {
  const isLoggedIn = localStorage.getItem('loggedIn') === 'true'
  if (to.meta.requiresAuth && !isLoggedIn) {
    next('/login')
  } else {
    next()
  }
})

export default router
