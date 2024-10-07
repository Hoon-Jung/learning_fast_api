import { createRouter, createWebHistory } from "vue-router";

import Home from "@/vues/Home.vue";
import Body from "@/vues/Body.vue";
import CreatePost from "@/vues/CreatePost.vue";
import UserCreate from "@/vues/UserCreate.vue";
import UserLogin from "@/vues/UserLogin.vue";
import PostChange from "@/vues/PostChange.vue";
import ReplyChange from "@/vues/ReplyChange.vue";

const routes = [
  {
    path: "/",
    redirect: "list/0",
  },
  {
    path: "/list/:category_id",
    name: "Home",
    component: Home,
    props: true,
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
  },
  {
    path: "/user-login",
    name: "UserLogin",
    component: UserLogin,
  },
  {
    path: "/update_post/:post_id",
    name: "PostUpdate",
    component: PostChange,
    props: true,
  },
  {
    path: "/update_reply/:reply_id",
    name: "ReplyUpdate",
    component: ReplyChange,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;