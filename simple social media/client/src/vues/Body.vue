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
    <li v-for="comment in post.comments" :key="comment.id">
      {{ comment.content }}
    </li>
  </ul>
</template>