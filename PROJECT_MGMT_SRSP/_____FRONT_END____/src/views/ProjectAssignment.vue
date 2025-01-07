<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-2xl font-bold mb-4">Assign Project</h1>
    <form @submit.prevent="assignProject">
      <div class="mb-4">
        <label class="block font-medium">Select Project:</label>
        <select v-model="selectedProject" class="p-2 border rounded w-full">
          <option v-for="project in projects" :key="project.id" :value="project.id">
            {{ project.name }}
          </option>
        </select>
      </div>
      <div class="mb-4">
        <label class="block font-medium">Select User:</label>
        <select v-model="selectedUser" class="p-2 border rounded w-full">
          <option v-for="user in users" :key="user.id" :value="user.id">
            {{ user.username }}
          </option>
        </select>
      </div>
      <button class="px-4 py-2 bg-blue-500 text-white rounded">Assign</button>
    </form>
  </div>
</template>

<script>
import axios from "../utils/axios";

export default {
  data() {
    return {
      projects: [],
      users: [],
      selectedProject: null,
      selectedUser: null,
    };
  },
  async created() {
    this.projects = (await axios.get("/projects/")).data;
    this.users = (await axios.get("/users/")).data; // Replace with the correct API for users
  },
  methods: {
    async assignProject() {
      try {
        await axios.post("/project-owners/", {
          project: this.selectedProject,
          user: this.selectedUser,
        });
        alert("Project assigned successfully!");
      } catch (error) {
        console.error("Error assigning project:", error);
      }
    },
  },
};
</script>
