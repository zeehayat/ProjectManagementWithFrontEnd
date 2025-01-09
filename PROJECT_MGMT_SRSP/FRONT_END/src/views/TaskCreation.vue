<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Add Task to {{ project.name }}</h1>
    <form @submit.prevent="addTask">
      <div class="mb-4">
        <label class="block font-medium mb-2">Task Name</label>
        <input v-model="taskName" type="text" class="w-full p-3 border rounded" placeholder="Enter task name" required />
      </div>

      <div class="mb-4">
        <label class="block font-medium mb-2">Description</label>
        <textarea v-model="description" class="w-full p-3 border rounded" placeholder="Enter task description"></textarea>
      </div>

      <button
        type="submit"
        class="w-full py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-600"
      >
        Add Task
      </button>
    </form>
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
      taskName: "",
      description: "",
    };
  },
  async created() {
    try {
      // Fetch project details
      const response = await axiosInstance.get(`/projects/${this.projectId}/`);
      this.project = response.data;
    } catch (error) {
      console.error("Failed to fetch project details:", error.response || error);
    }
  },
  methods: {
    async addTask() {
      try {
        const taskData = {
          name: this.taskName,
          description: this.description,
          project: this.project.id,
        };
        const response = await axiosInstance.post("/tasks/", taskData);
        alert("Task added successfully!");
        this.taskName = "";
        this.description = "";
      } catch (error) {
        console.error("Failed to add task:", error.response.data || error);
        if (error.response && error.response.data) {
          alert(JSON.stringify(error.response.data));
        }
      }
    },
  },
};
</script>

<style scoped>
button {
  margin-top: 1rem;
}
</style>
