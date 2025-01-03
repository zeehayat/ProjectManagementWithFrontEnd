<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-2xl font-bold mb-4">Notifications</h1>
    <ul>
      <li
        v-for="notification in notifications"
        :key="notification.id"
        class="py-2 border-b"
      >
        <div>
          <span :class="{ 'font-bold': !notification.is_read }">
            {{ notification.message }}
          </span>
          <button
            v-if="!notification.is_read"
            @click="markAsRead(notification.id)"
            class="px-2 py-1 ml-4 bg-green-500 text-white rounded"
          >
            Mark as Read
          </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "../utils/axios";

export default {
  data() {
    return {
      notifications: [],
    };
  },
  async created() {
    const response = await axios.get("/notifications/");
    this.notifications = response.data;
  },
  methods: {
    async markAsRead(notificationId) {
      try {
        await axios.put(`/notifications/${notificationId}/read/`);
        const notification = this.notifications.find(
          (n) => n.id === notificationId
        );
        notification.is_read = true; // Update the UI
      } catch (error) {
        console.error("Error marking notification as read:", error);
      }
    },
  },
};
</script>
