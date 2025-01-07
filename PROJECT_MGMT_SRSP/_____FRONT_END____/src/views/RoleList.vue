<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-2xl font-bold mb-4">Roles Management</h1>
    <form @submit.prevent="createRole" class="mb-4">
      <input
        v-model="newRole"
        type="text"
        placeholder="Enter role name"
        class="p-2 border rounded mr-2"
      />
      <button class="px-4 py-2 bg-blue-500 text-white rounded">Add Role</button>
    </form>
    <ul>
      <li v-for="role in roles" :key="role.id" class="py-2">
        {{ role.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "../utils/axios";

export default {
  data() {
    return {
      roles: [],
      newRole: "",
    };
  },
  async created() {
    const response = await axios.get("/roles/");
    this.roles = response.data;
  },
  methods: {
    async createRole() {
      try {
        const response = await axios.post("/roles/", { name: this.newRole });
        this.roles.push(response.data); // Update the list
        this.newRole = ""; // Clear the input
      } catch (error) {
        console.error("Error creating role:", error);
      }
    },
  },
};
</script>
