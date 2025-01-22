<template>
  <div class="h-screen flex bg-gray-100">
    <!-- Sidebar -->
    <div
      :class="['fixed h-full bg-white shadow transition-transform duration-300', isOpen ? 'translate-x-0' : '-translate-x-full']"
      style="width: 250px;"
    >
      <button @click="toggleMenu" class="absolute top-4 right-4 p-2">
        <span class="text-black">&times;</span>
      </button>
      <nav class="p-6 space-y-4">
        <h1 class="text-lg font-bold text-black">Menu</h1>
        <ul>
          <li>
            <router-link
              to="/dashboard"
              class="block p-3 rounded text-gray-700 hover:bg-gray-200"
            >
              Dashboard
            </router-link>
          </li>
          <li>
            <router-link
              to="/projects"
              class="block p-3 rounded text-gray-700 hover:bg-gray-200"
            >
              Projects
            </router-link>
          </li>
          <li>
            <router-link
              to="/tasks"
              class="block p-3 rounded text-gray-700 hover:bg-gray-200"
            >
              Tasks
            </router-link>
          </li>
          <li>
            <a @click="handleLogout" class="block p-3 rounded text-gray-700 hover:bg-gray-200">
              Logout
            </a>
          </li>
        </ul>
      </nav>
    </div>

    <!-- Content Area -->
    <div class="flex-1">
      <header class="bg-gray-800 text-white p-4 flex items-center">
        <button @click="toggleMenu" class="p-2 mr-4">
          <span class="text-white">&#9776;</span>
        </button>
        <h1 class="text-xl font-bold text-white">SRSP Project Management Application</h1>
      </header>
      <main class="p-6">
        <!-- Removed duplicate router-view -->
      </main>
      <div>
        <button @click="toggleDropdown">Notifications ({{ notifications.length }})</button>
        <div v-if="isDropdownVisible">
          <ul>
            <li v-for="notification in notifications" :key="notification.id">
              {{ notification.message }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { logout } from "@/utils/axios";
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      isOpen: false,
      notifications: [],
      isDropdownVisible: false,
    };
  },
  async created() {
    const response = await axiosInstance.get("/notifications/");
    this.notifications = response.data;
  },
  methods: {
    toggleMenu() {
      this.isOpen = !this.isOpen;
    },
    toggleDropdown() {
      this.isDropdownVisible = !this.isDropdownVisible;
    },
    async handleLogout() {
      await logout();
    },
  },
};
</script>

<style scoped>
/* Minimalist Color Theme */
body {
  background-color: #f5f5f5; /* Light gray */
  color: #333; /* Dark gray */
}

nav ul li a {
  color: gray;
}

nav ul li a:hover {
  color: black;
}
</style>
