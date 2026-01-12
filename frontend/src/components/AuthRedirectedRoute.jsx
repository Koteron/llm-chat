import { Outlet, Navigate } from 'react-router-dom';
import { useEffect } from 'react';
import useAuthStore from '../state/useAuthStore';

const AuthRedirectedRoute = ({ route, requireLogin }) => {
  const { isLoggedIn } = useAuthStore();

  useEffect(() => {
    if (requireLogin && !isLoggedIn || !requireLogin && isLoggedIn) {
      return <Navigate to={route} replace />;
    }

  }, [isLoggedIn]);

  return <Outlet />;
};

export default AuthRedirectedRoute;