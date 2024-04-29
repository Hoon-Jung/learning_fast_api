import { createRouter, createWebHistory } from "vue-router";
import Home from "@/vues/Home.vue";
import Body from "@/vues/Body.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/body/:post_id",
    name: "Body",
    component: Body,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;