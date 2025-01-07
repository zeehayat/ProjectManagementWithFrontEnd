<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-2xl font-bold mb-4">Create Project</h1>
    <form @submit.prevent="createProject">
      <div class="mb-4">
        <label class="block font-medium">Project Name:</label>
        <input
          v-model="name"
          type="text"
          placeholder="Enter project name"
          class="p-2 border rounded w-full"
        />
      </div>
      <div class="mb-4">
        <label class="block font-medium">Description:</label>
        <textarea
          v-model="description"
          placeholder="Enter project description"
          class="p-2 border rounded w-full"
        ></textarea>
      </div>
      <button class="px-4 py-2 bg-blue-500 text-white rounded">Create</button>
    </form>
  </div>
</template>

<script>
import axios from "../utils/axios";

export default {
  data() {
    return {
      name: "",
      description: "",
    };
  },
  methods: {
    async createProject() {
      try {
        await axios.post("/projects/", {
          name: this.name,
          description: this.description,
        });
        alert("Project created successfully!");
      } catch (error) {
        console.error("Error creating project:", error);
      }
    },
  },
};
</script>
