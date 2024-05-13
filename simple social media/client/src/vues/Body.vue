<script>
export default{
  props: {
    post_id: {
      type: String,
      required: true
    }
  },
  data() {
    return{
      post: {}
    }
  },
  created() {
    this.getPost()
  },
  methods: {
    getPost(){
      fetch(`http://localhost:8000/api/post/detail/${this.post_id}`).then((response) => {
        response.json().then((json) => {
            this.post = json;
            });
        });
    }
  },
};
</script>

<template>
  <h1> {{ this.post.subject }}</h1>
  <div> {{ this.post.content }}</div>
  <ul>
<<<<<<< HEAD
    <li v-for="comment in post.comments" :key="comment.id">
=======
    <li v-for="comment in post.replies" :key="comment.id">
>>>>>>> d2012c2 (Debugged everything (only UI is left))
      {{ comment.content }}
    </li>
  </ul>
</template>