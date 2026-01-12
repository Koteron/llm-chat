import Login from '../pages/Login.jsx';
import Register from '../pages/Register.jsx';
import Chats from '../pages/Chats.jsx';
import { Navigate } from 'react-router-dom';
import AuthRedirectedRoute from '../components/AuthRedirectedRoute.jsx';

const routesConfig = [
  {
    path: "/",
    element: <Navigate to="/login" replace />,
  },
  {
    element: <AuthRedirectedRoute route={'/chats'} requireLogin={false} />,
    children: [
      { path: "/login", element: <Login /> },
      { path: "/register", element: <Register /> },
    ]
  },
  {
    element: <AuthRedirectedRoute route={'/login'} requireLogin={true} />,
    children: [
      { path: "/chat", element: <Chats /> },
    ]
  },
];

export default routesConfig;