<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-6">Dashboard</h1>

    <!-- Task Summary -->
    <div class="mb-6">
      <h2 class="text-xl font-semibold mb-4">Task Summary</h2>
      <div class="grid grid-cols-3 gap-4">
        <div class="p-4 bg-white shadow rounded text-center">
          <h3 class="text-lg font-bold">Pending</h3>
          <p class="text-2xl">{{ taskSummary.pending }}</p>
        </div>
        <div class="p-4 bg-white shadow rounded text-center">
          <h3 class="text-lg font-bold">In Progress</h3>
          <p class="text-2xl">{{ taskSummary.in_progress }}</p>
        </div>
        <div class="p-4 bg-white shadow rounded text-center">
          <h3 class="text-lg font-bold">Completed</h3>
          <p class="text-2xl">{{ taskSummary.completed }}</p>
        </div>
      </div>
    </div>

    <!-- Overdue Tasks -->
    <div class="mb-6">
      <h2 class="text-xl font-semibold mb-4">Overdue Tasks</h2>
      <ul>
  <li
    v-for="task in overdueTasks"
    :key="task.id"
    class="p-4 bg-white shadow rounded mb-4"
  >
    <p class="text-lg font-bold">{{ task.name }}</p>
    <p>Due Date: {{ task.due_date }}</p>
    <p>Assigned To: {{ task.assigned_to }}</p>
    <button
      @click="viewTaskHistory(task.id)"
      class="mt-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
    >
      View History
    </button>
    <button
      v-if="task.extension_status === 'Pending'"
      disabled
      class="mt-2 ml-2 px-4 py-2 bg-gray-500 text-white rounded cursor-not-allowed"
    >
      Extension Requested
    </button>
    <button
      v-else
      @click="openExtensionModal(task.id)"
      class="mt-2 ml-2 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
    >
      Request Extension
    </button>
    <button
      @click="viewTaskDetails(task.id)"
      class="mt-2 ml-2 px-4 py-2 bg-indigo-500 text-white rounded hover:bg-indigo-600"
    >
      View Details
    </button>
  </li>
</ul>
    </div>

    <!-- Task History Modal -->
    <div
      v-if="isHistoryModalVisible"
      class="fixed inset-0 bg-gray-500 bg-opacity-50 flex justify-center items-center"
    >
      <div class="bg-white p-6 rounded shadow-lg w-3/4">
        <h3 class="text-lg font-bold mb-4">Task History</h3>
        <ul>
          <li v-for="entry in taskHistory" :key="entry.id">
            <p>{{ entry.timestamp }}: {{ entry.change }}</p>
          </li>
        </ul>
        <button @click="isHistoryModalVisible = false" class="mt-4 px-4 py-2 bg-red-500 text-white rounded">
          Close
        </button>
      </div>
    </div>

    <!-- Extension Request Modal -->
    <div
      v-if="isExtensionModalVisible"
      class="fixed inset-0 bg-gray-500 bg-opacity-50 flex justify-center items-center"
    >
      <div class="bg-white p-6 rounded shadow-lg w-1/2">
        <h3 class="text-lg font-bold mb-4">Request Task Extension</h3>
        <form @submit.prevent="submitExtensionRequest">
          <div class="mb-4">
            <label class="block font-medium mb-2">Additional Days</label>
            <input v-model="extensionDays" type="number" min="1" class="w-full p-3 border rounded" required />
          </div>
          <div class="mb-4">
            <label class="block font-medium mb-2">Reason</label>
            <textarea v-model="extensionReason" class="w-full p-3 border rounded" required></textarea>
          </div>
          <div class="flex justify-end">
            <button
              type="button"
              @click="isExtensionModalVisible = false"
              class="px-4 py-2 bg-gray-500 text-white rounded mr-2"
            >
              Cancel
            </button>
            <button type="submit" class="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      taskSummary: {pending: 0, in_progress: 0, completed: 0},
      overdueTasks: [],
      taskHistory: [],
      isHistoryModalVisible: false,
      isExtensionModalVisible: false,
      selectedTaskId: null,
      extensionDays: 1,
      extensionReason: "",
    };
  },
  async created() {
   try {
    const response = await axiosInstance.get("/dashboard/");
    console.log("Dashboard Data:", response.data); // Debugging log
    this.taskSummary = response.data.task_summary;
    this.overdueTasks = response.data.overdue_tasks.map((task) => {
      if (task.assigned_to === this.$store.state.user.username) {
        task.assigned_to = "Assigned to me";
      }
      return task;
    });
    console.log("Overdue Tasks:", this.overdueTasks); // Debugging log
  } catch (error) {
    console.error("Failed to load dashboard data:", error.response || error);
  }
  },
  methods: {
    async viewTaskHistory(taskId) {
      this.isHistoryModalVisible = true;
      try {
        const response = await axiosInstance.get(`/tasks/${taskId}/history/`);
        this.taskHistory = response.data;
      } catch (error) {
        console.error("Failed to fetch task history:", error.response || error);
        alert("Failed to load task history.");
        this.isHistoryModalVisible = false;
      }
    },
    openExtensionModal(taskId) {
      this.selectedTaskId = taskId;
      this.isExtensionModalVisible = true;
    },
    async submitExtensionRequest() {
      try {
        await axiosInstance.post(`/tasks/${this.selectedTaskId}/extension/`, {
          additional_days: this.extensionDays,
          reason: this.extensionReason,
        });
        alert("Extension request submitted successfully!");
        this.isExtensionModalVisible = false;
        this.extensionDays = 1;
        this.extensionReason = "";
        this.fetchTasks();
      } catch (error) {
        console.error("Failed to submit extension request:", error.response || error);
        alert("Failed to submit extension request.");
      }
    },
    async fetchTasks() {
      try {
        const response = await axiosInstance.get("/dashboard/");
        this.overdueTasks = response.data.overdue_tasks.map((task) => {
          if (task.assigned_to === this.$store.state.user.username) {
            task.assigned_to = "Assigned to me";
          }
          return task;
        });
      } catch (error) {
        console.error("Failed to refresh tasks:", error.response || error);
      }
    },
    async viewTaskDetails(taskId) {
      // Logic to navigate or fetch task details
      alert(`Viewing details for task ID: ${taskId}`);
    },
  },
};
</script>

<style scoped>
button {
  margin-top: 1rem;
}
</style>
