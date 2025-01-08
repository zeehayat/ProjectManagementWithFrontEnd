<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Task Details</h1>

    <!-- Notes Section -->
    <div class="mb-6">
      <h2 class="text-xl font-semibold mb-2">Notes</h2>
      <textarea
        v-model="task.assigneeNotes"
        placeholder="Notes from Assignee"
        class="w-full p-3 border rounded mb-4"
      ></textarea>
      <textarea
        v-model="task.assignedPersonNotes"
        placeholder="Notes from Assigned Person"
        class="w-full p-3 border rounded"
      ></textarea>
    </div>

    <!-- Media Attachments -->
    <div class="mb-6">
      <h2 class="text-xl font-semibold mb-2">Attachments</h2>
      <input type="file" multiple @change="uploadAttachments" />
      <ul>
        <li v-for="attachment in task.attachments" :key="attachment.id">
          <a :href="attachment.url" target="_blank" class="text-blue-500 underline">
            {{ attachment.fileName }}
          </a>
        </li>
      </ul>
    </div>

    <!-- GPS Coordinates -->
    <div class="mb-6">
      <h2 class="text-xl font-semibold mb-2">GPS Coordinates</h2>
      <p>
        Latitude: {{ task.gpsLatitude || "N/A" }} <br />
        Longitude: {{ task.gpsLongitude || "N/A" }}
      </p>
    </div>

    <!-- Request Additional Time -->
    <div>
      <h2 class="text-xl font-semibold mb-2">Request Additional Time</h2>
      <form @submit.prevent="requestAdditionalTime">
        <input
          type="number"
          v-model="additionalDays"
          placeholder="Enter additional days"
          class="p-3 border rounded mb-4"
        />
        <textarea
          v-model="additionalReason"
          placeholder="Reason for request"
          class="w-full p-3 border rounded mb-4"
        ></textarea>
        <button
          type="submit"
          class="w-full py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-600"
        >
          Request Time
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "@/utils/axios";

export default {
  data() {
    return {
      task: {
        assigneeNotes: "",
        assignedPersonNotes: "",
        attachments: [],
        gpsLatitude: null,
        gpsLongitude: null,
      },
      additionalDays: "",
      additionalReason: "",
    };
  },
  async created() {
    // Fetch task details
    const response = await axios.get("/tasks/1"); // Replace with dynamic task ID
    this.task = response.data;
  },
  methods: {
    async uploadAttachments(event) {
      const files = event.target.files;
      const formData = new FormData();
      Array.from(files).forEach((file) => formData.append("attachments", file));

      const response = await axios.post(`/tasks/${this.task.id}/attachments/`, formData);
      this.task.attachments = response.data;
    },
    async requestAdditionalTime() {
      const response = await axios.post(`/tasks/${this.task.id}/extension-requests/`, {
        additional_days: this.additionalDays,
        reason: this.additionalReason,
      });
      alert("Request submitted!");
      this.additionalDays = "";
      this.additionalReason = "";
    },
  },
};
</script>
