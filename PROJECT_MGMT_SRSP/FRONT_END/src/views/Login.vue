<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="bg-white p-6 rounded shadow-lg w-96">
      <h1 class="text-2xl font-bold mb-4 text-center">Login</h1>
      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label class="block font-medium mb-2">Username</label>
          <input v-model="username" type="text" class="w-full p-3 border rounded" placeholder="Enter your username" required />
        </div>
        <div class="mb-4">
          <label class="block font-medium mb-2">Password</label>
          <input v-model="password" type="password" class="w-full p-3 border rounded" placeholder="Enter your password" required />
        </div>
        <button type="submit" class="w-full py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-600">
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axiosInstance.post("/token/", {
          username: this.username,
          password: this.password,
        });
        localStorage.setItem("accessToken", response.data.access);
        localStorage.setItem("refreshToken", response.data.refresh);
        this.$router.push("/tasks"); // Navigate to /tasks after successful login
      } catch (error) {
        console.error("Login failed:", error.response || error);
      }
    },
  },
};
</script>
