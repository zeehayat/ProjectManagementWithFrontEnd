<template>

  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-6">My Tasks </h1>

    <!-- Filters -->
    <div class="mb-6 flex gap-4">
      <select v-model="statusFilter" class="p-2 border rounded">
        <option value="">All Statuses T</option>
        <option value="Pending">Pending</option>
        <option value="In Progress">In Progress</option>
        <option value="Completed">Completed</option>
      </select>
      <input
        v-model="completionDateFilter"
        type="date"
        class="p-2 border rounded"
        placeholder="Filter by Completion Date"
      />
    </div>

    <!-- Projects and Tasks -->
    <div v-if="Object.keys(filteredTasks).length > 0">
      <div v-for="(tasks, projectName) in filteredTasks" :key="projectName" class="mb-8">
        <h2 class="text-xl font-semibold mb-4">{{ projectName }}</h2>
        <div v-for="task in tasks" :key="task.id" class="p-4 bg-white shadow rounded mb-4">
          <h3 class="text-lg font-bold">{{ task.name }}</h3>
          <p>Status: {{ task.status }}</p>
          <p>Assigned By: {{ task.assigned_by?.username || "N/A" }}</p>
          <p>Due Date: {{ task.due_date || "N/A" }}</p>
           <button @click="openUpdateModal(task.id)" class="px-4 py-2 bg-green-500 text-white rounded" v-if="task.status!='Completed'">
          Update Task
        </button>
          <button class="px-4 py-2 bg-green-500 text-white rounded" >
          View Details
        </button>
        </div>
      </div>
    </div>

    <!-- No Tasks Message -->
    <div v-else>
      <p class="text-gray-500">No tasks found matching your criteria.</p>
    </div>
  </div>
  <!-- Task Update Modal -->
 <!-- Update Modal -->
    <TaskUpdateModal
      v-if="isUpdateModalVisible"
      :taskId="selectedTaskId"
      :isVisible="isUpdateModalVisible"
      @task-updated="fetchTasks"
      @close="isUpdateModalVisible = false"
    />

</template>
<script>
import axiosInstance from "@/utils/axios";
import TaskUpdateModal from "@/components/TaskUpdateModal.vue";

export default {
    components: { TaskUpdateModal },

  data() {
    return {
      tasks: {}, // Grouped tasks from the API
      statusFilter: "",
      completionDateFilter: "",
       isUpdateModalVisible: false,
      selectedTaskId: null,
    };
  },
  computed: {
    filteredTasks() {
      const filtered = {};
      Object.keys(this.tasks).forEach((projectName) => {
        filtered[projectName] = this.tasks[projectName].filter((task) => {
          const matchesStatus =
            this.statusFilter === "" || task.status === this.statusFilter;
          const matchesDate =
            !this.completionDateFilter ||
            new Date(task.due_date) <= new Date(this.completionDateFilter);
          return matchesStatus && matchesDate;
        });
      });
      return filtered;
    },
  },
  async created() {
    try {
      const response = await axiosInstance.get("/tasks/user/");
      this.tasks = response.data; // Assign tasks data to the tasks object
      console.log("Fetched tasks:", this.tasks); // Debugging
    } catch (error) {
      console.error("Failed to fetch tasks:", error.response || error);
    }
  },
  methods: {
    openUpdateModal(taskId) {
      this.selectedTaskId = taskId;
      this.isUpdateModalVisible = true;
    },
    fetchTasks() {
            this.isUpdateModalVisible = false; // Hide modal after task fetch

    },
  },
};
</script>
