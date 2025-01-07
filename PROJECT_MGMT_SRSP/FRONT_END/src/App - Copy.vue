
<template>
  <div id="app">
    <Menubar />
    <router-view />
  </div>

</template>


<script>
import Menubar from "./components/Menubar.vue";

export default {
  components: {
    Menubar,
  },
};
</script>

<style>
/* Optional global styles */
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
</style>