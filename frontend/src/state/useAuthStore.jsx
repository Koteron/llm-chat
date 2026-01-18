import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { refreshToken } from '../services/api';

const useAuthStore = create(persist(
  (set) => ({
    isLoggedIn: false,
    access: null,
    refresh: null,
    login: (access, refresh) => set({ isLoggedIn: true, access: access, refresh: refresh }),
    logout: () => set({ isLoggedIn: false, user: null }),
    doRefresh: async (refresh) => {
      const data = await refreshToken(refresh)
      set({ isLoggedIn: true, access: data.access, refresh: data.refresh })
    },
  }),
  {
    name: 'auth-storage',
  }
));

export default useAuthStore;