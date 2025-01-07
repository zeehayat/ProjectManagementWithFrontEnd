<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-2xl font-bold mb-4">Create Task</h1>
    <form @submit.prevent="createTask">
      <div class="mb-4">
        <label class="block font-medium">Task Name:</label>
        <input
          v-model="name"
          type="text"
          placeholder="Enter task name"
          class="p-2 border rounded w-full"
        />
      </div>
      <div class="mb-4">
        <label class="block font-medium">Project:</label>
        <select v-model="selectedProject" class="p-2 border rounded w-full">
          <option v-for="project in projects" :key="project.id" :value="project.id">
            {{ project.name }}
          </option>
        </select>
      </div>
      <button class="px-4 py-2 bg-blue-500 text-white rounded">Create Task</button>
    </form>
  </div>
</template>

<script>
import axios from "../utils/axios";

export default {
  data() {
    return {
      name: "",
      selectedProject: null,
      projects: [],
    };
  },
  async created() {
    this.projects = (await axios.get("/projects/")).data;
  },
  methods: {
    async createTask() {
      try {
        await axios.post("/tasks/", {
          name: this.name,
          project: this.selectedProject,
        });
        alert("Task created successfully!");
      } catch (error) {
        console.error("Error creating task:", error);
      }
    },
  },
};
</script>
