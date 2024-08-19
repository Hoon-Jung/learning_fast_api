<template>
    <div class="container my-3">
      <h4>Edit Post</h4>
      <error_component :error="error" />
      <form @submit.prevent="updatePost">
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
        <button type="submit" class="btn btn-primary">Save Changes</button>
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
      subject: "",
      content: "",
      error: { detail:[] },
    }
  },
  mounted() {
    let url = "/api/post/detail/" + this.post_id;
    fastapi("get", url, {}, (json) => {
        this.subject = json.subject;
        this.content = json.content;
    });
  },
  methods: {
    updatePost(){
      let params={
        subject: this.subject,
        content: this.content,
        post_id: this.post_id,
      }

      fastapi("put", `/api/post/update`, params, () => {
        this.$router.push("/body/" + this.post_id);
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
