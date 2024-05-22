<script>
import fastapi from '../../lib/api';
export default{
  data() {
    return {
        allposts: [],
    }
  },
  created() {
    this.getPosts();
  },
  methods: {
    getPosts() {
      fastapi("get", "/api/post/list", {}, (json) => {
        this.allposts = json;
      });
        // fetch("http://localhost:8000/api/post/list").then((response) => {
        // response.json().then((json) => {
        //     this.allposts = json;
        //     });
        // });
    },
  },
};
</script>

<template>
  <ul>
    <li v-for="post in allposts" :key="post.id">
        <router-link :to="'/body/' + post.id">{{ post.subject }}</router-link>
    </li>
  </ul>
</template>