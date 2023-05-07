<template>
  <v-app>
    <v-main>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
      <p class="mt-5 text-h3 font-weight-bold text-center">IDENTIFYING FAKE JOBS</p>
      </div>

      <v-spacer></v-spacer>
      <v-btn @click="home" class="mr-2">home</v-btn>
      <v-btn @click="visualizations" class="ml-2">visualizations</v-btn>
    </v-app-bar>
<!-- 
    <v-main>
      <div class="ma-5">
        <main-form/>

      </div>
    </v-main> -->
    <router-view/></v-main>
  </v-app>
</template>

<script>
// import MainForm from './components/MainForm.vue';

export default {
  name: 'App',
  components: {
    // MainForm,
  },
  methods: {
    visualizations() {
      this.$router.push({ name: "graphs" });
    },
    home() {
      this.$router.push({ name: "home" });
    },
  }
};
</script>
