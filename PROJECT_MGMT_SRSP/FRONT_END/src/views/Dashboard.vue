<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-3xl font-bold mb-6">Dashboard</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div v-for="project in projects" :key="project.id" class="p-4 bg-white shadow-md rounded-lg">
        <h2 class="font-bold text-xl">{{ project.name }}</h2>
        <p class="text-gray-600">{{ project.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from '../utils/axios';

export default {
  data() {
    return {
      projects: [],
    };
  },
  async created() {
    try {
      const response = await axios.get('projects/');
      this.projects = response.data;
    } catch (error) {
      console.error('Failed to fetch projects:', error);
    }
  },
};
</script>
