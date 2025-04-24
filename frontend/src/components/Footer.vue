<template>
    <footer class="footer">
      <div class="footer-content">
        <p>&copy; 2025 Expense Tracker. All Rights Reserved.</p>
        <div class="social-links">
          <a href="https://twitter.com" target="_blank">Twitter</a>
          <a href="https://facebook.com" target="_blank">Facebook</a>
          <a href="https://github.com" target="_blank">GitHub</a>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: "Footer"
  };
  </script>
  
  <style scoped>
  .footer {
    background-color: var(--bg-color);
    color: var(--text-color);
    padding: 20px;
    text-align: center;
    margin-top: 20px;
  }
  
  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .social-links {
    margin-top: 10px;
  }
  
  .social-links a {
    margin: 0 15px;
    text-decoration: none;
    color: var(--text-color);
    font-size: 1rem;
    transition: color 0.3s;
  }
  
  .social-links a:hover {
    color: var(--primary-color);
  }
  </style>
  