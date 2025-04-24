<template>
  <div>
    <!-- Header -->
    <Header :loggedIn="loggedIn" @logged-out="handleLogout" />

    <!-- Dark Mode Toggle Button -->
    <button class="mode-toggle" @click="toggleDarkMode">
      {{ isDark ? '🌙 Dark Mode' : '☀️ Light Mode' }}
    </button>

    <!-- Features Section -->
    <Features />

    <!-- This is where your different pages will show based on the route -->
    <router-view @logged-in="handleLogin" />

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import Features from './components/Features.vue'

export default {
  components: {
    Navbar,
    Header,
    Footer,
    Features
  },
  data() {
    return {
      loggedIn: false,
      isDark: false
    }
  },
  methods: {
    handleLogin() {
      this.loggedIn = true
      localStorage.setItem('loggedIn', 'true')
      this.$router.push('/dashboard')
    },
    handleLogout() {
      this.loggedIn = false
      localStorage.removeItem('loggedIn')
      this.$router.push('/login')
    },
    toggleDarkMode() {
      this.isDark = !this.isDark
      document.body.classList.toggle('dark', this.isDark)
      localStorage.setItem('darkMode', this.isDark)
    }
  },
  mounted() {
    this.loggedIn = localStorage.getItem('loggedIn') === 'true'
    this.isDark = localStorage.getItem('darkMode') === 'true'
    document.body.classList.toggle('dark', this.isDark)
  }
}
</script>

<style scoped>
.mode-toggle {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: transparent;
  border: none;
  font-size: 16px;
  cursor: pointer;
}
</style>
