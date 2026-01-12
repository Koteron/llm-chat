import { create } from 'zustand';
import { persist } from 'zustand/middleware';

const useAuthStore = create(persist(
  (set) => ({
    isLoggedIn: false,
    access: null,
    refresh: null,
    login: (access, refresh) => set({ isLoggedIn: true, access: access, refresh: refresh }),
    logout: () => set({ isLoggedIn: false, user: null }),
  }),
  {
    name: 'auth-storage',
  }
));

export default useAuthStore;