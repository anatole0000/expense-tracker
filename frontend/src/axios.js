import axios from 'axios';

// Set the base URL for the API
const api = axios.create({
  baseURL: 'http://localhost:5000', // Change to your Flask server's URL
  withCredentials: true,  // To allow cookie-session if using authentication
});

export default api;
