<template>
    <header class="header">
      <div class="logo">
        <h1>Expense Tracker</h1>
      </div>
      <nav>
        <ul class="nav-links">
          <li><router-link to="/dashboard" v-if="isLoggedIn">Dashboard</router-link></li>
          <li>
          <router-link to="/analytics">Analytics</router-link> <!-- New Analytics link -->
          </li>
          <li><router-link to="/login" v-if="!isLoggedIn">Login</router-link></li>
          <li><router-link to="/register" v-if="!isLoggedIn">Register</router-link></li>
          <li><button v-if="isLoggedIn" @click="logout">Logout</button></li>
        </ul>
      </nav>
    </header>
  </template>
  
  <script>
  export default {
    name: 'Header',
    data() {
      return {
        isLoggedIn: localStorage.getItem('loggedIn') === 'true'
      };
    },
    methods: {
      logout() {
        localStorage.removeItem('loggedIn'); // Clear login state
        this.isLoggedIn = false; // Update state
        this.$router.push('/login'); // Redirect to login page
      }
    },
    watch: {
      // Watch for changes in loggedIn status
      '$route'(to, from) {
        this.isLoggedIn = localStorage.getItem('loggedIn') === 'true';
      }
    }
  };
  </script>
  
  <style scoped>
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
    background-color: var(--bg-color);
    color: var(--text-color);
  }
  
  .logo h1 {
    font-size: 1.8rem;
    font-weight: 600;
    margin: 0;
  }
  
  .nav-links {
    list-style: none;
    display: flex;
  }
  
  .nav-links li {
    margin: 0 15px;
  }
  
  .nav-links li a,
  .nav-links li button {
    text-decoration: none;
    color: var(--text-color);
    font-size: 1rem;
    transition: color 0.3s;
  }
  
  .nav-links li a:hover,
  .nav-links li button:hover {
    color: var(--primary-color);
  }
  
  button {
    background: none;
    border: none;
    cursor: pointer;
  }
  </style>
  