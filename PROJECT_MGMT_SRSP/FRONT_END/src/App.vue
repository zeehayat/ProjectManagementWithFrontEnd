<template>
  <div id="app" class="h-screen flex flex-col">
    <Menubar v-if="isAuthenticated" />

    <div class="flex-1 flex justify-center items-center bg-gray-100">
      <router-view />
    </div>
  </div>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";
import Menubar from "./components/Menubar.vue";

export default {
  components: {
    Menubar,
  },
  setup() {
    const store = useStore();
    const isAuthenticated = computed(() => store.state.isAuthenticated);
    return { isAuthenticated };
  },
};
</script>