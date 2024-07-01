import { createRouter, createWebHistory } from "vue-router";

import Home from "@/vues/Home.vue";
import Body from "@/vues/Body.vue";
import CreatePost from "@/vues/CreatePost.vue";
import UserCreate from "@/vues/UserCreate.vue"

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
    path: "/post-add",
    name: "CreatePost",
    component: CreatePost,
    props: true,
  },
  {
    path: "/user-create",
    name: "UserCreate",
    component: UserCreate,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;