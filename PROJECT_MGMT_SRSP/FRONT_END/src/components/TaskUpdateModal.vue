<template>
  <div v-if="isVisible" class="fixed inset-0 bg-gray-500 bg-opacity-50 flex justify-center items-center">
    <div class="bg-white p-6 rounded shadow-lg w-96">
      <h2 class="text-xl font-semibold mb-4">Update Task</h2>

      <!-- Status -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Status</label>
        <select v-model="status" class="w-full p-2 border rounded">
          <option value="Pending">Pending</option>
          <option value="In Progress">In Progress</option>
          <option value="Completed">Completed</option>
        </select>
      </div>

      <!-- Assignee Notes -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Assignee Notes</label>
        <textarea v-model="assigneeNotes" class="w-full p-2 border rounded"></textarea>
      </div>

      <!-- Assigned Person Notes -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Assigned Person Notes</label>
        <textarea v-model="assignedPersonNotes" class="w-full p-2 border rounded"></textarea>
      </div>

      <!-- Attachments -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Attachments</label>
        <input type="file" @change="handleAttachments" multiple />
      </div>

      <!-- Actions -->
      <div class="flex justify-end gap-4">
        <button @click="isVisible = false" class="px-4 py-2 bg-gray-300 rounded">Cancel</button>
        <button @click="updateTask" class="px-4 py-2 bg-blue-500 text-white rounded">Update</button>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  props: {
    taskId: {
      type: Number,
      required: true,
    },
    isVisible: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      status: "Pending",
      assigneeNotes: "",
      assignedPersonNotes: "",
      attachments: [],
    };
  },
  methods: {
    handleAttachments(event) {
      this.attachments = Array.from(event.target.files);
    },
    async updateTask() {
      const formData = new FormData();
      formData.append("status", this.status);
      formData.append("assignee_notes", this.assigneeNotes);
      formData.append("assigned_person_notes", this.assignedPersonNotes);

      this.attachments.forEach((file, index) => {
        formData.append(`attachments[${index}]`, file);
      });

      try {
        await axiosInstance.patch(`/tasks/${this.taskId}/update/`, formData, {
          headers: { "Content-Type": "multipart/form-data" },
        });
        alert("Task updated successfully!");
        this.isVisible = false;
        this.$emit("task-updated");
      } catch (error) {
        console.error("Failed to update task:", error.response || error);
        alert("Failed to update task.");
      }
    },
  },
};
</script>
