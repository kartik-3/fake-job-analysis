<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-img src="./assets/JobVerifyLogo.jpeg" max-height="60px" max-width="60px" style="margin-right: 10px"></v-img>
      <div class="d-flex align-center">
        <p class="mt-5 text-h3 font-weight-bold text-center">JobVerify</p>
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-row>
      <v-col cols="2">
        <v-navigation-drawer class="mt-16" permanent>
          <v-list dense nav>
            <v-list-item @click="home" :class="`elevation-2`" class="transition-swing">
              <v-list-item-icon>
                <v-icon> mdi-home</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title class="text-h6">
                  HOME
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>
            <v-list-item @click="predict" :class="`elevation-2`" class="transition-swing">
              <v-list-item-icon>
                <v-icon>mdi-tab-search</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title class="text-h6">
                  PREDICT
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>
            <v-list-item @click="visualizations" :class="`elevation-2`" class="transition-swing">
              <v-list-item-icon>
                <v-icon> mdi-chart-bar</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title class="text-h6">
                  VISUALIZATIONS
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-divider></v-divider>
          </v-list>

        </v-navigation-drawer>

      </v-col>
      <v-col cols="10">

        <v-main>
          <router-view />
        </v-main>
      </v-col>
    </v-row>
  </v-app>
</template>



<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'App',
  computed: {
    ...mapState('jobs', ['dataByCols', 'dataById', 'notProvidedCounts', 'providedCounts']),
  },
  methods: {
    ...mapActions('jobs', ['UPDATE_dataByCols', 'UPDATE_dataById', 'UPDATE_notProvidedCounts', 'UPDATE_providedCounts']),
    visualizations() {
      this.$router.push({ name: "graphs" });
    },
    home() {
      this.$router.push({ name: "home" });
    },
    predict() {
      this.$router.push({ name: "predict" });
    },
  }
};
</script>
