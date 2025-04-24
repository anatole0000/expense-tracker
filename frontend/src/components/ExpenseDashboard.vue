<template>
  <div>
    <h2>Your Expenses</h2>

    <!-- Filter by Month -->
    <label>Filter by Month:</label>
    <input type="month" v-model="selectedMonth" @change="loadExpenses" />

    <!-- Expense Form -->
    <form @submit.prevent="addExpense">
      <input v-model="amount" placeholder="Amount" type="number" required />
      
      <!-- Category Dropdown -->
      <select v-model="category" required>
        <option disabled value="">Select Category</option>
        <option v-for="cat in categories" :key="cat.id" :value="cat.name">
          {{ cat.name }}
        </option>
      </select>
      
      <input v-model="description" placeholder="Description" />
      <input v-model="date" type="date" required />
      <button type="submit">Add Expense</button>
    </form>

    <!-- Category Form -->
    <form @submit.prevent="addCategory" style="margin-top: 1em;">
      <input v-model="newCategory" placeholder="New Category" required />
      <button type="submit">Add Category</button>
    </form>

    <!-- Category List with Delete -->
    <ul>
      <li v-for="cat in categories" :key="cat.id">
        {{ cat.name }}
        <button @click="deleteCategory(cat.id)">🗑</button>
      </li>
    </ul>

    <!-- Expense List -->
    <ul>
      <li v-for="e in expenses" :key="e.id">
        {{ e.date }} - {{ e.category }} - ${{ e.amount }} ({{ e.description }})
      </li>
    </ul>

    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      amount: '',
      category: '',
      description: '',
      date: '',
      selectedMonth: '',
      expenses: [],
      categories: [],
      newCategory: ''
    }
  },
  methods: {
    async loadExpenses() {
      let url = 'http://localhost:5000/expenses'
      if (this.selectedMonth) {
        url += `?month=${this.selectedMonth}`
      }
      try {
        const res = await axios.get(url, { withCredentials: true })
        this.expenses = res.data
      } catch (err) {
        console.error('Load expenses error:', err)
      }
    },
    async addExpense() {
      try {
        await axios.post('http://localhost:5000/expenses', {
          amount: this.amount,
          category: this.category,
          description: this.description,
          date: this.date
        }, { withCredentials: true })
        this.loadExpenses()
        this.amount = this.category = this.description = this.date = ''
      } catch (err) {
        console.error('Add expense error:', err)
      }
    },
    async loadCategories() {
      try {
        const res = await axios.get('http://localhost:5000/categories', { withCredentials: true })
        this.categories = res.data
      } catch (err) {
        console.error('Load categories error:', err)
      }
    },
    async addCategory() {
      try {
        await axios.post('http://localhost:5000/categories', {
          name: this.newCategory
        }, { withCredentials: true })
        this.loadCategories()
        this.newCategory = ''
      } catch (err) {
        console.error('Add category error:', err)
      }
    },
    async deleteCategory(id) {
      try {
        await axios.delete(`http://localhost:5000/categories/${id}`, { withCredentials: true })
        this.loadCategories()
      } catch (err) {
        console.error('Delete category error:', err)
      }
    },
    async logout() {
      try {
        await axios.get('http://localhost:5000/logout', { withCredentials: true })
        window.location.reload()
      } catch (err) {
        console.error('Logout error:', err)
      }
    }
  },
  mounted() {
    this.loadExpenses()
    this.loadCategories()
  }
}
</script>
<style scoped>
/* General Layout */
div {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1.5rem;
  border-radius: 12px;
  background: #f9f9f9;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', sans-serif;
}

h2 {
  text-align: center;
  color: #333;
}

/* Inputs and Selects */
input,
select {
  display: block;
  width: 100%;
  padding: 0.5rem;
  margin: 0.5rem 0;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  box-sizing: border-box;
}

select {
  background-color: white;
}

/* Buttons */
button {
  padding: 0.6rem 1.2rem;
  margin-top: 0.5rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}

/* Expense and Category Lists */
ul {
  list-style: none;
  padding-left: 0;
  margin-top: 1.5rem;
}

li {
  background: #ffffff;
  padding: 0.75rem;
  margin-bottom: 0.5rem;
  border-left: 5px solid #4caf50;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Trash button inside list */
li button {
  background-color: #e74c3c;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  font-size: 0.9rem;
}

li button:hover {
  background-color: #c0392b;
}

/* Logout button */
button:last-of-type {
  display: block;
  margin: 2rem auto 0;
  background-color: #f44336;
}

button:last-of-type:hover {
  background-color: #d32f2f;
}
</style>
