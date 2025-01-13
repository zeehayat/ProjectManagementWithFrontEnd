// TaskCreation.vue
<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Add Task to {{ project.name }}</h1>
    <form @submit.prevent="addTask">
      <!-- Task Name -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Task Name</label>
        <input
          v-model="taskName"
          type="text"
          class="w-full p-3 border rounded"
          placeholder="Enter task name"
          required
        />
      </div>

      <!-- Description -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Description</label>
        <textarea
          v-model="description"
          class="w-full p-3 border rounded"
          placeholder="Enter task description"
        ></textarea>
      </div>

      <!-- Assigned To -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Assign To</label>
        <select v-model="assignedTo" class="w-full p-3 border rounded">
          <option value="" disabled>Select a user</option>
          <option v-for="user in users" :key="user.id" :value="user.id">
            {{ user.username }}
          </option>
        </select>
      </div>

      <!-- Due Date -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Due Date</label>
        <input
          v-model="dueDate"
          type="date"
          class="w-full p-3 border rounded"
        />
      </div>

      <!-- Status -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Status</label>
        <select v-model="status" class="w-full p-3 border rounded">
          <option value="Pending">Pending</option>
          <option value="In Progress">In Progress</option>
          <option value="Completed">Completed</option>
        </select>
      </div>

      <!-- Assignee Notes -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Assignee Notes</label>
        <textarea
          v-model="assigneeNotes"
          class="w-full p-3 border rounded"
          placeholder="Add assignee notes"
        ></textarea>
      </div>

      <!-- Assigned Person Notes -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Assigned Person Notes</label>
        <textarea
          v-model="assignedPersonNotes"
          class="w-full p-3 border rounded"
          placeholder="Add assigned person notes"
        ></textarea>
      </div>

      <!-- GPS Latitude -->
      <div class="mb-4">
        <label class="block font-medium mb-2">GPS Latitude</label>
        <input
          v-model="gpsLatitude"
          type="number"
          step="any"
          class="w-full p-3 border rounded"
          placeholder="Enter GPS latitude"
        />
      </div>

      <!-- GPS Longitude -->
      <div class="mb-4">
        <label class="block font-medium mb-2">GPS Longitude</label>
        <input
          v-model="gpsLongitude"
          type="number"
          step="any"
          class="w-full p-3 border rounded"
          placeholder="Enter GPS longitude"
        />
      </div>

      <!-- Attachments -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Attachments</label>
        <input
          type="file"
          multiple
          @change="handleAttachments"
          class="w-full p-3 border rounded"
        />
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
      assignedTo: "",
      dueDate: "",
      status: "Pending",
      assigneeNotes: "",
      assignedPersonNotes: "",
      gpsLatitude: "",
      gpsLongitude: "",
      attachments: [],
      users: [],
    };
  },
  async created() {
    try {
      // Fetch project details
      const projectResponse = await axiosInstance.get(`/projects/${this.projectId}/`);
      this.project = projectResponse.data;

      // Fetch users
      const usersResponse = await axiosInstance.get("/users/");
      this.users = usersResponse.data;
    } catch (error) {
      console.error("Failed to fetch data:", error.response || error);
    }
  },
  methods: {
    handleAttachments(event) {
      this.attachments = Array.from(event.target.files);
    },
    async addTask() {
      const formData = new FormData();
      formData.append("name", this.taskName);
      formData.append("description", this.description);
      formData.append("assigned_to", this.assignedTo);
      formData.append("project", this.project.id);
      formData.append("due_date", this.dueDate);
      formData.append("status", this.status);
      formData.append("assignee_notes", this.assigneeNotes);
      formData.append("assigned_person_notes", this.assignedPersonNotes);
      formData.append("gps_latitude", this.gpsLatitude);
      formData.append("gps_longitude", this.gpsLongitude);

      this.attachments.forEach((file, index) => {
        formData.append(`attachments[${index}]`, file);
      });

      try {
        const response = await axiosInstance.post("/tasks/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        alert("Task added successfully!");
        this.resetForm();
      } catch (error) {
        console.error("Failed to add task:", error.response || error);
        if (error.response && error.response.data) {
          alert(JSON.stringify(error.response.data));
        }
      }
    },
    resetForm() {
      this.taskName = "";
      this.description = "";
      this.assignedTo = "";
      this.dueDate = "";
      this.status = "Pending";
      this.assigneeNotes = "";
      this.assignedPersonNotes = "";
      this.gpsLatitude = "";
      this.gpsLongitude = "";
      this.attachments = [];
    },
  },
};
</script>

<style scoped>
button {
  margin-top: 1rem;
}
</style>
