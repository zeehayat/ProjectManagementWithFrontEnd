<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Assign Task</h1>
    <form @submit.prevent="assignTask">
      <!-- Select Task -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Task</label>
        <select v-model="taskId" class="w-full p-3 border rounded" required>
          <option value="" disabled>Select a task</option>
          <option v-for="task in tasks" :key="task.id" :value="task.id">
            {{ task.name }}
          </option>
        </select>
      </div>

      <!-- Select User -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Assign To</label>
        <select v-model="assignedTo" class="w-full p-3 border rounded" required>
          <option value="" disabled>Select a user</option>
          <option v-for="user in users" :key="user.id" :value="user.id">
            {{ user.username }}
          </option>
        </select>
      </div>

      <!-- Submit Button -->
      <button
        type="submit"
        class="w-full py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-600"
      >
        Assign Task
      </button>
    </form>
  </div>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      taskId: "",
      assignedTo: "",
      tasks: [],
      users: [],
    };
  },
  async created() {
    try {
      const tasksResponse = await axiosInstance.get("/tasks/?project=1"); // Filter tasks by project ID
      this.tasks = tasksResponse.data;

      const usersResponse = await axiosInstance.get("/users/");
      this.users = usersResponse.data;
    } catch (error) {
      console.error("Failed to fetch data:", error.response || error);
    }
  },
  methods: {
    async assignTask() {
      try {
        const response = await axiosInstance.patch(`/tasks/${this.taskId}/`, {
          assigned_to: this.assignedTo,
        });
        alert("Task assigned successfully!");
      } catch (error) {
        console.error("Failed to assign task:", error.response.data || error);
      }
    },
  },
};
</script>
