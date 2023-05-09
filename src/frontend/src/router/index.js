// Routers for navigation
import Vue from 'vue'
import VueRouter from 'vue-router'
import MainForm from '../components/MainForm'
import GraphVisuals from '../components/GraphVisuals'
import HomePage from '../components/HomePage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: {
      name: "home"
    }
  },
  {
    path: '/graphs',
    name: 'graphs',
    component: GraphVisuals
  },
  {
    path: '/predict',
    name: 'predict',
    component: MainForm
  },
  {
    path: '/home',
    name: 'home',
    component: HomePage
  }
]

const router = new VueRouter({
  mode: 'history',
  base:  process.env.BASE_URL,
  routes
})

export default router
