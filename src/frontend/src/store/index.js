// Store for storing state variables
import Vue from 'vue'
import Vuex from 'vuex'
import jobs from "./modules/jobs.module"

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    jobs
  }
})