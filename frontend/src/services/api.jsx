import axios from 'axios';

export const apiBaseURL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: `${apiBaseURL}`,
});

export const loginUser = async (username, password) => {
  try {
    const response = await api.post('/token/create', {
      "username": username,
      "password": password,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const registerUser = async (email, login, password) => {
  try {
    const response = await api.post('/users/register', {
      "email": email,
      "login": login,
      "password": password,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getConversationList = async (jwtToken) => {
  try {
    const response = await api.get('/conversation/',{
      headers: {
        "Authorization": `Bearer ${jwtToken}`
      }
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getConversationDetail = async (conversation_id, jwtToken) => {
  try {
    const response = await api.get(`/conversation/${conversation_id}/`,{
      headers: {
        "Authorization": `Bearer ${jwtToken}`
      }
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const createConversation = async (title, jwtToken) => {
  try {
    const response = await api.post(`/conversation/`,
      {
        title: title
      },{
      headers: {
        "Authorization": `Bearer ${jwtToken}`
      }
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const sendMessage = async (messageText, conversation_id, jwtToken) => {
  try {
    const response = await api.post(`/message/`,
      {
        conversation_id: conversation_id,
        text: messageText
      },{
      headers: {
        "Authorization": `Bearer ${jwtToken}`
      }
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};