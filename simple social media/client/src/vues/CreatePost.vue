<template>
    <div class="container my-3">
      <h4>Create a Post</h4>
      <ErrorComponent :error="error" />
      <form @submit.prevent="createPost">
        <div class="mb-3">
          <label for="subject" class="form-label">Title</label>
          <input
            type="text"
            class="form-control"
            id="subject"
            v-model="subject"
            required
          />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content</label>
          <textarea
            class="form-control"
            id="content"
            rows="10"
            v-model="content"
            required
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Create Post</button>
      </form>
    </div>
  </template>

<script>
import fastapi from '../../lib/api';
import error_component from "../components/error_component.vue";
export default{
  components: {
    error_component,
  },
  props: {
    post_id: {
      type: String,
      required: true
    }
  },
  data() {
    return{
      post: {},
      error: { detail:[] },
    }
  },
  created() {
  },
  methods: {
    createPost(){
      let params={
        subject: this.subject,
        content: this.content,
      }

      fastapi("post", `/api/post/add`, params, () => {
        this.$router.push("/");
      },
      (err) => {
        this.error = err; 
      });

      // fetch(`http://localhost:8000/api/reply/add/${this.post_id}`, options).then((response) => {
      //   console.log(response);
      //   this.getPost();
      // }).catch((error) => {
      //   console.log("Error:", error);
      // })
    }
  },
};
</script>
