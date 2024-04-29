<script>
export default{
  data() {
    return {
        allposts: [],
    }
  },
  created() {
  },
  methods: {
    getBody() {
        fetch("http://localhost:8000/api/post/").then((response) => {
        response.json().then((json) => {
            this.allposts = json;
            });
        });
    },
  },
};
</script>

<template>
  <ul>
    <li v-for="post in allposts">{{ post.content }}</li>
  </ul>
</template>