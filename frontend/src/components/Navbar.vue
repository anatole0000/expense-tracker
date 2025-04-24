<template>
    <nav class="navbar">
      <router-link to="/register"><UserPlus class="icon" /> Register</router-link>
      <router-link to="/login"><LogIn class="icon" /> Login</router-link>
      <router-link v-if="loggedIn" to="/dashboard"><LayoutDashboard class="icon" /> Dashboard</router-link>
      <button v-if="loggedIn" @click="logout"><LogOut class="icon" /> Logout</button>
    </nav>
  </template>
  
  <script>
  import axios from 'axios'
  import { UserPlus, LogIn, LogOut, LayoutDashboard } from 'lucide-vue-next'
  
  export default {
    props: ['loggedIn'],
    components: { UserPlus, LogIn, LogOut, LayoutDashboard },
    methods: {
      async logout() {
        await axios.get('http://localhost:5000/logout', { withCredentials: true })
        this.$emit('logged-out')
      }
    }
  }
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    background: #f9f9f9;
    border-bottom: 1px solid #ddd;
  }
  .icon {
    width: 1rem;
    height: 1rem;
    margin-right: 0.3rem;
    vertical-align: middle;
  }
  button, a {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 1rem;
    text-decoration: none;
    border: none;
    background: none;
    cursor: pointer;
  }
  </style>
  