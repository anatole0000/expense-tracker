<template>
    <section id="features" class="features-section">
      <h2>Key Features</h2>
      <div class="features-container">
        <div class="feature-item">
          <h3>Track Your Expenses</h3>
          <p>Record all your expenses easily with our user-friendly interface.</p>
        </div>
        <div class="feature-item">
          <h3>Set Budget Categories</h3>
          <p>Organize your expenses by categories for better management.</p>
        </div>
        <div class="feature-item">
          <h3>Generate Reports</h3>
          <p>Generate monthly or yearly reports to analyze your spending patterns.</p>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: "Features"
  };
  </script>
  
  <style scoped>
  .features-section {
    background-color: var(--bg-light-color);
    padding: 50px 20px;
    text-align: center;
  }
  
  .features-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 20px;
  }
  
  .feature-item {
    background-color: var(--bg-color);
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 250px;
    text-align: center;
  }
  
  .feature-item h3 {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  .feature-item p {
    font-size: 1rem;
    color: var(--text-muted);
  }
  </style>
  