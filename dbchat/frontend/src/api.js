import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api', // Assuming the backend runs on port 8000
  headers: {
    'Content-Type': 'application/json',
  },
});

export const connectToDatabase = (db_path) => {
  return apiClient.post('/connect', { db_path });
};

export const sendQuery = (session_id, prompt) => {
  return apiClient.post('/query', { session_id, prompt });
};