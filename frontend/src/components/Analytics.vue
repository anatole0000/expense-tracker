<template>
    <div class="analytics">
      <h2>Analytics / Summary</h2>
  
      <!-- Total Spent -->
      <div class="summary-item">
        <h3>Total Spent</h3>
        <p>${{ totalSpent }}</p>
      </div>
  
      <!-- Spending by Category -->
      <div class="spending-by-category">
        <h3>Spending by Category</h3>
        <ul>
          <li v-for="category in spendingByCategory" :key="category.category">
            {{ category.category }}: ${{ category.total_spent }}
          </li>
        </ul>
      </div>
  
      <!-- Monthly Summary -->
      <div class="monthly-summary">
        <h3>Monthly Summary</h3>
        <ul>
          <li v-for="month in monthlySummary" :key="month.month">
            {{ month.month }}: ${{ month.total_spent }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        totalSpent: 0,
        spendingByCategory: [],
        monthlySummary: []
      }
    },
    methods: {
      async fetchAnalyticsData() {
        try {
          // Get total spent
          const totalSpentRes = await axios.get('/api/total_spent')
          this.totalSpent = totalSpentRes.data.total_spent
  
          // Get spending by category
          const spendingByCategoryRes = await axios.get('/api/spending_by_category')
          this.spendingByCategory = spendingByCategoryRes.data.spending_by_category
  
          // Get monthly summary
          const monthlySummaryRes = await axios.get('/api/monthly_summary')
          this.monthlySummary = monthlySummaryRes.data.monthly_summary
        } catch (err) {
          console.error('Error fetching analytics data:', err)
        }
      }
    },
    mounted() {
      this.fetchAnalyticsData()
    }
  }
  </script>
  
  <style scoped>
  .analytics {
    padding: 20px;
  }
  
  .summary-item, .spending-by-category, .monthly-summary {
    margin-bottom: 20px;
  }
  
  h3 {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    font-size: 1rem;
    margin-bottom: 5px;
  }
  </style>
  