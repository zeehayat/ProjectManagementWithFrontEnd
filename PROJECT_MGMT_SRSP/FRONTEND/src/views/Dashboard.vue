<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-3xl font-bold mb-6">Dashboard</h1>

    <!-- Key Metrics -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
      <div class="p-4 bg-white shadow-md rounded">
        <h2 class="text-lg font-bold">Total Projects</h2>
        <p class="text-2xl">{{ metrics.totalProjects }}</p>
      </div>
      <div class="p-4 bg-white shadow-md rounded">
        <h2 class="text-lg font-bold">Total Tasks</h2>
        <p class="text-2xl">{{ metrics.totalTasks }}</p>
      </div>
      <div class="p-4 bg-white shadow-md rounded">
        <h2 class="text-lg font-bold">Pending Notifications</h2>
        <p class="text-2xl">{{ metrics.pendingNotifications }}</p>
      </div>
    </div>

    <!-- Task Status Distribution -->
    <div class="p-6 bg-white shadow-md rounded mb-6">
      <h2 class="text-xl font-bold mb-4">Task Status Distribution</h2>
      <canvas id="taskStatusChart"></canvas>
    </div>

    <!-- Quick Actions -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <button
        @click="navigate('/create-project')"
        class="p-4 bg-blue-500 text-white font-bold rounded"
      >
        Create Project
      </button>
      <button
        @click="navigate('/assign-task')"
        class="p-4 bg-green-500 text-white font-bold rounded"
      >
        Assign Task
      </button>
      <button
        @click="navigate('/notifications')"
        class="p-4 bg-yellow-500 text-white font-bold rounded"
      >
        View Notifications
      </button>
    </div>
  </div>
</template>

<script>
import axios from "../utils/axios";
import Chart from "chart.js/auto";

export default {
  data() {
    return {
      metrics: {
        totalProjects: 0,
        totalTasks: 0,
        pendingNotifications: 0,
      },
      taskStatusData: {},
    };
  },
  async created() {
    await this.fetchMetrics();
    await this.renderTaskStatusChart();
  },
  methods: {
    async fetchMetrics() {
      try {
        const [projects, tasks, notifications] = await Promise.all([
          axios.get("/projects/"),
          axios.get("/tasks/"),
          axios.get("/notifications/"),
        ]);

        this.metrics.totalProjects = projects.data.length;
        this.metrics.totalTasks = tasks.data.length;
        this.metrics.pendingNotifications = notifications.data.filter(
            (n) => !n.is_read
        ).length;

        this.taskStatusData = tasks.data.reduce((acc, task) => {
          acc[task.status] = (acc[task.status] || 0) + 1;
          return acc;
        }, {});
      } catch (error) {
        console.error("Error fetching metrics:", error);
      }
    },
    async renderTaskStatusChart() {
    const ctx = document.getElementById("taskStatusChart").getContext("2d");
    if (this.chart) {
    this.chart.destroy();
    }
    const labels = Object.keys(this.taskStatusData); // Status names (e.g., Pending, In Progress, Completed)
    const data = Object.values(this.taskStatusData); // Counts of each status

    new Chart(ctx, {
      type: "doughnut", // Chart type
      data: {
        labels, // Assign the labels
        datasets: [
          {
            data, // Assign the data
            backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"], // Colors for each segment
          },
        ],
      },
    });
  },
    navigate(path) {
      this.$router.push(path);
    },
  },
};
</script>
