<template>
    <div class="container my-3">
      <h4>질문 등록</h4>
      <ErrorComponent :error="error" />
      <form @submit.prevent="postQuestion">
        <div class="mb-3">
          <label for="subject" class="form-label">제목</label>
          <input
            type="text"
            class="form-control"
            id="subject"
            v-model="subject"
            required
          />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">내용</label>
          <textarea
            class="form-control"
            id="content"
            rows="10"
            v-model="content"
            required
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">저장하기</button>
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
        content: this.content,
      }

      fastapi("post", `/api/reply/add/${this.post_id}`, params, () => {
        this.content = "";
        this.getPost();
        this.error = { detail:[] };
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
