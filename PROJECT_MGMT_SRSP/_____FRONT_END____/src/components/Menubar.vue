<template>
  <nav class="bg-blue-600 text-white p-4">
    <div class="container mx-auto flex justify-between items-center">
      <!-- Logo -->
      <div class="text-lg font-bold">Project Manager</div>

      <!-- Navigation Links -->
      <ul class="flex space-x-4">
        <li>
          <router-link to="/dashboard" class="hover:underline">Dashboard</router-link>
        </li>
        <li>
          <router-link to="/create-project" class="hover:underline">Create Project</router-link>
        </li>
        <li>
          <router-link to="/assign-task" class="hover:underline">Assign Task</router-link>
        </li>
        <li>
          <router-link to="/notifications" class="hover:underline">Notifications</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Menubar",
};
</script>
