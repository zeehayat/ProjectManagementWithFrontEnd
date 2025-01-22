<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Update Task: {{ task.name }}</h1>

    <form @submit.prevent="updateTask">
      <!-- Status -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Status</label>
        <select v-model="task.status" class="w-full p-3 border rounded">
          <option value="Pending">Pending</option>
          <option value="In Progress">In Progress</option>
          <option value="Completed">Completed</option>
        </select>
      </div>

      <!-- Assignee Notes -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Assignee Notes</label>
        <textarea
          v-model="task.assignee_notes"
          class="w-full p-3 border rounded"
          placeholder="Update assignee notes"
        ></textarea>
      </div>

      <!-- Assigned Person Notes -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Assigned Person Notes</label>
        <textarea
          v-model="task.assigned_person_notes"
          class="w-full p-3 border rounded"
          placeholder="Update assigned person notes"
        ></textarea>
      </div>

      <!-- Add Attachments -->
      <div class="mb-4">
        <label class="block font-medium mb-2">Add Attachments</label>
        <input
          type="file"
          multiple
          @change="handleAttachments"
          class="w-full p-3 border rounded"
        />
      </div>

      <!-- Current Attachments -->
      <div v-if="task.attachments.length" class="mb-4">
        <label class="block font-medium mb-2">Current Attachments</label>
        <ul>
          <li v-for="attachment in task.attachments" :key="attachment.id" class="flex justify-between items-center">
            <a :href="attachment.file" target="_blank" class="text-blue-500">{{ attachment.name }}</a>
            <button
              @click.prevent="removeAttachment(attachment.id)"
              class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
            >
              Remove
            </button>
          </li>
        </ul>
      </div>

      <button
        type="submit"
        class="w-full py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-600"
      >
        Update Task
      </button>
    </form>
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
  },
  data() {
    return {
      task: {
        name: "",
        status: "Pending",
        assignee_notes: "",
        assigned_person_notes: "",
        attachments: [],
      },
      newAttachments: [],
      removeAttachmentsList: [],
    };
  },
  async created() {
    try {
      const response = await axiosInstance.get(`/tasks/${this.taskId}/`);
      this.task = response.data;
    } catch (error) {
      console.error("Failed to load task:", error.response || error);
    }
  },
  methods: {
    handleAttachments(event) {
      this.newAttachments = Array.from(event.target.files);
    },
    async removeAttachment(attachmentId) {
      this.removeAttachmentsList.push(attachmentId);
      this.task.attachments = this.task.attachments.filter((attachment) => attachment.id !== attachmentId);
    },
    async updateTask() {
      const formData = new FormData();
      formData.append("status", this.task.status);
      formData.append("assignee_notes", this.task.assignee_notes);
      formData.append("assigned_person_notes", this.task.assigned_person_notes);

      this.newAttachments.forEach((file, index) => {
        formData.append(`attachments[${index}]`, file);
      });

      this.removeAttachmentsList.forEach((attachmentId, index) => {
        formData.append(`remove_attachments[${index}]`, attachmentId);
      });

      try {
        await axiosInstance.patch(`/tasks/${this.taskId}/update/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        alert("Task updated successfully!");
      } catch (error) {
        console.error("Failed to update task:", error.response || error);
        alert("Failed to update task. Please try again.");
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
