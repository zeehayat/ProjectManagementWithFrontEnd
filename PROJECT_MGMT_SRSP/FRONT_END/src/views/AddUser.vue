<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Add User</h1>
    <form @submit.prevent="addUser">
      <div class="mb-4">
        <label class="block font-medium mb-2">Username</label>
        <input v-model="username" type="text" class="w-full p-3 border rounded" required />
      </div>
      <div class="mb-4">
        <label class="block font-medium mb-2">Email</label>
        <input v-model="email" type="email" class="w-full p-3 border rounded" required />
      </div>
      <div class="mb-4">
        <label class="block font-medium mb-2">Password</label>
        <input v-model="password" type="password" class="w-full p-3 border rounded" required />
      </div>
      <button type="submit" class="w-full py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-600">
        Add User
      </button>
    </form>
  </div>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  methods: {
    async addUser() {
      try {
        const response = await axiosInstance.post("/users/add/", {
          username: this.username,
          email: this.email,
          password: this.password,
        });
        alert("User added successfully!");
        this.username = "";
        this.email = "";
        this.password = "";
      } catch (error) {
        console.error("Failed to add user:", error.response || error);
      }
    },
  },
};
</script>
