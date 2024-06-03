import { createRouter, createWebHistory } from "vue-router";

import Home from "@/vues/Home.vue";
import Body from "@/vues/Body.vue";
import CreatePost from "@/vues/CreatePost.vue";

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
  {
    path: "/create_post",
    name: "CreatePost",
    component: CreatePost,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;