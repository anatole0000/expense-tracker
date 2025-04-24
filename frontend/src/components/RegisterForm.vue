<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Register</button>
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
    async register() {
      try {
        const res = await axios.post('http://localhost:5000/register', {
          email: this.email,
          password: this.password
        }, { withCredentials: true })
        this.message = res.data.message
      } catch (err) {
        this.message = 'Registration failed'
      }
    }
  }
}
</script>
