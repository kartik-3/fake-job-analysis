import Vue from 'vue'
import VueRouter from 'vue-router'
import MainForm from '../components/MainForm'
import GraphVisuals from '../components/GraphVisuals'

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
  },{
    path: '/home',
    name: 'home',
    component: MainForm
  }
]

const router = new VueRouter({
  mode: 'history',
  base:  process.env.BASE_URL,
  routes
})

export default router
