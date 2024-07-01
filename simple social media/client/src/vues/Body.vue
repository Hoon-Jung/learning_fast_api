<!-- <template>
  <h1> {{ this.post.subject }}</h1>
  <div> {{ this.post.content }}</div>
  <ul>
    <li v-for="comment in post.replies" :key="comment.id">
      {{ comment.content }}
    </li>
    <error_component :error="error"/>
  </ul>
  <form @submit.prevent="addReply">
    <textarea rows="15" v-model="content"></textarea>
    <input type="submit" value="Add Comment" />
  </form>
</template>

<style>
    textarea {
        width:100%;
    }
    input[type=submit] {
        margin-top:10px;
    }    
</style>
 -->

<template>
  <div class="container my-3">
    <div class="mt-4">
      <router-link to="/" class="btn btn-secondary"> < Back </router-link>
    </div>
    <h2 class="border-bottom py-2">{{ post.subject }}</h2>
    <div class="card my-3">
      <div class="card-body">
        <div class="card-text" style="white-space: pre-line">
          {{ post.content }}
        </div>
        <div class="d-flex justify-content-end">
          <div class="badge bg-light text-dark p-2">
            {{ formatDate(post.created_at) }}
          </div>
        </div>
      </div>
    </div>
        <h5 class="border-bottom my-3 py-2">
          {{ post.replies?.length }} replies
        </h5>
        <div class="card my-3" v-for="reply in post.replies" :key="reply.id">
          <div class="card-body">
            <div class="card-text" style="white-space: pre-line">
              {{ reply.content }}
            </div>
            <div class="d-flex justify-content-end">
              <div class="badge bg-light text-dark p-2">
                {{ formatDate(reply.created_at) }}
              </div>
            </div>
          </div>
        </div>
    <!-- 답변 등록 -->
        <error_component :error="error" />
        <form @submit.prevent="addReply" class="my-3">
          <div class="mb-3">
            <textarea rows="10" v-model="content" class="form-control" />
          </div>
          <input type="submit" value="답변등록" class="btn btn-primary" />
        </form>
      </div>
</template>


<script>
import moment from "moment";
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
      content: "",
      error: { detail:[] },
    }
  },
  created() {
    this.getPost()
  },
  methods: {
    formatDate(dt){
      return moment(dt).startOf("hour").fromNow();
    },
    getPost(){
      fastapi("get", `/api/post/detail/${this.post_id}`, {}, (json) => {
        this.post = json;
      });
    },
    addReply(){
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
