<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
      <p>{{ message }}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      email: '',
      password: '',
      message: ''
    }
  },
  methods: {
    async login() {
      try {
        const res = await axios.post('http://localhost:5000/login', {
          email: this.email,
          password: this.password
        }, { withCredentials: true })
        this.$emit('logged-in')
        this.message = res.data.message
      } catch (err) {
        this.message = 'Login failed'
      }
    }
  }
}
</script>
