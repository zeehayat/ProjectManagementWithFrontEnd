<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-2xl font-bold mb-4">Assign Role</h1>
    <form @submit.prevent="assignRole">
      <label>User:</label>
      <select v-model="selectedUser" class="p-2 border rounded mb-4">
        <option v-for="user in users" :key="user.id" :value="user.id">
          {{ user.username }}
        </option>
      </select>
      <label>Role:</label>
      <select v-model="selectedRole" class="p-2 border rounded mb-4">
        <option v-for="role in roles" :key="role.id" :value="role.id">
          {{ role.name }}
        </option>
      </select>
      <button class="px-4 py-2 bg-blue-500 text-white rounded">
        Assign Role
      </button>
    </form>
  </div>
</template>

<script>
import axios from "../utils/axios";

export default {
  data() {
    return {
      users: [],
      roles: [],
      selectedUser: null,
      selectedRole: null,
    };
  },
  async created() {
    this.users = (await axios.get("/users/")).data; // API to fetch users
    this.roles = (await axios.get("/roles/")).data; // API to fetch roles
  },
  methods: {
    async assignRole() {
      try {
        await axios.post("/user-roles/", {
          user: this.selectedUser,
          role: this.selectedRole,
        });
        alert("Role assigned successfully!");
      } catch (error) {
        console.error("Error assigning role:", error);
      }
    },
  },
};
</script>
