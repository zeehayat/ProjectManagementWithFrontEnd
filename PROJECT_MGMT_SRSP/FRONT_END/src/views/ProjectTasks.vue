<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Tasks for {{ project.name }}</h1>
    <ul>
      <li v-for="task in tasks" :key="task.id" class="mb-2">
        <div class="p-4 bg-white rounded shadow">
          <h2 class="text-lg font-semibold">{{ task.name }}</h2>
          <p>{{ task.description }}</p>
          <p class="text-gray-500">Assigned to: {{ task.assigned_to.username || 'Unassigned' }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      project: {},
      tasks: [],
    };
  },
  async created() {
    try {
      // Fetch project details
      const projectResponse = await axiosInstance.get(`/projects/${this.projectId}/`);
      this.project = projectResponse.data;

      // Fetch tasks for the project
      const tasksResponse = await axiosInstance.get(`/tasks/?project=${this.projectId}`);
      this.tasks = tasksResponse.data;
    } catch (error) {
      console.error("Failed to fetch data:", error.response || error);
    }
  },
};
</script>

<style scoped>
.task {
  margin-bottom: 1rem;
}
</style>

