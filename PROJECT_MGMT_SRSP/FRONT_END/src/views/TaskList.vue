<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-6">Task List</h1>

    <!-- Task List -->
    <ul>
      <li v-for="task in tasks" :key="task.id" class="p-4 bg-white shadow rounded mb-4">
        <p class="text-lg font-bold">{{ task.name }}</p>
        <p>Status: {{ task.status }}</p>
        <p>Assigned To: {{ task.assigned_to || 'Unassigned' }}</p>
        <router-link
          :to="{ name: 'TaskUpdate', params: { taskId: task.id } }"
          class="text-blue-500 underline"
        >
          Edit Task
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      tasks: [],
    };
  },
  async created() {
    try {
      const response = await axiosInstance.get("/tasks/");
      this.tasks = response.data;
    } catch (error) {
      console.error("Failed to load tasks:", error.response || error);
    }
  },
};
</script>

<style scoped>
li {
  list-style: none;
  padding: 1rem;
  margin-bottom: 1rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
