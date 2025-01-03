
<template>
  <div id="app">
    <Menubar />
    <router-view />
  </div>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
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