<template>
  <div id="app" class="h-screen flex flex-col">
    <Menubar v-if="isAuthenticated" />

    <div class="flex-1 flex justify-center items-center bg-gray-100">
      <router-view />
    </div>
  </div>
</template>

<script>
import Menubar from "./components/Menubar.vue";
import { mapState } from "vuex";

export default {
  components: {
    Menubar,
  },
  computed: {
    ...mapState(["isAuthenticated"]), // Maps isAuthenticated from store
  },
};
</script>