<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-2xl font-bold mb-4">Assign Task</h1>
    <form @submit.prevent="assignTask">
      <div class="mb-4">
        <label class="block font-medium">Select Task:</label>
        <select v-model="selectedTask" class="p-2 border rounded w-full">
          <option v-for="task in tasks" :key="task.id" :value="task.id">
            {{ task.name }}
          </option>
        </select>
      </div>
      <div class="mb-4">
        <label class="block font-medium">Assign To:</label>
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
      tasks: [],
      users: [],
      selectedTask: null,
      selectedUser: null,
    };
  },
  async created() {
    this.tasks = (await axios.get("/tasks/")).data;
    this.users = (await axios.get("/users/")).data;
  },
  methods: {
    async assignTask() {
      try {
        await axios.put(`/tasks/${this.selectedTask}/`, {
          assigned_to: this.selectedUser,
        });
        alert("Task assigned successfully!");
      } catch (error) {
        console.error("Error assigning task:", error);
      }
    },
  },
};
</script>
