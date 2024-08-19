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
            @{{ post.user?.username }} | {{ formatDate(post.created_at) }}
          </div>
        </div>

        <div class="my-3">
          <button class="btn btn-sm btn-outline-secondary" @click="likePost(post.id)">Likes 
            <span class="badge rounded-pill bg-success">{{ post.voter.length }}</span>
          </button>
        </div>

        <div class="my-3" v-if="post.user && $store.state.username === post.user.username">
        <router-link :to=" '/update_post/' + post.id " class="btn btn-sm btn-outline-secondary">Edit</router-link>
        <button class="btn btn-sm btn-outline-danger" @click="deletePost(post.id)">Delete</button>
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
                @{{ reply.user.username }} | {{ formatDate(reply.created_at) }}
              </div>
            </div>

            <div class="my-3">
              <button class="btn btn-sm btn-outline-secondary" @click="likeReply(reply.id)">Likes 
                <span class="badge rounded-pill bg-success">{{ reply.voter.length }}</span>
              </button>
            </div>

            <div class="my-3" v-if="reply.user && $store.state.username === reply.user.username">
            <router-link :to=" '/update_reply/' + reply.id " class="btn btn-sm btn-outline-secondary">Edit</router-link>
            <button class="btn btn-sm btn-outline-danger" @click="deleteReply(reply.id)">Delete</button>
            </div>

          </div>
        </div>
    <!-- Replies -->
        <error_component :error="error" />
        <form @submit.prevent="addReply" class="my-3">
          <div class="mb-3">
            <textarea rows="10" v-model="content" class="form-control"></textarea>
          </div>
          <input type="submit" value="Reply" class="btn btn-primary" />
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
      post: { voter: {} },
      content: "",
      error: { detail:[] },
    }
  },
  created() {
    this.getPost()
  },
  methods: {
    likePost(post_id){
      let params = {post_id: post_id};
      fastapi("post", `/api/post/like/`, params, () => {
        this.getPost();
      });
    },
    likeReply(reply_id){
      let params = {id: reply_id};
      fastapi("post", `/api/reply/like/`, params, () => {
        this.getPost();
      });
    },
    formatDate(dt){
      return moment(dt).startOf("minute").fromNow();
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
    },
    deletePost(post_id){
      if(confirm("Are you sure you would like to delete this post? This change cannot be undone.")){
        let url = "/api/post/delete";
        let params = {
          post_id: post_id,
        };
        fastapi("delete", url, params, () => {
          this.$router.push("/");
        },
        (err) => {
          this.error = err;
        },
      );
      }
    },
    deleteReply(reply_id){
      if(confirm("Are you sure you would like to delete this reply? This change cannot be undone.")){
        let url = "/api/reply/delete";
        let params = {
          id: reply_id,
        };
        fastapi("delete", url, params, () => {
          this.getPost();
        },
        (err) => {
          this.error = err;
        },
      );
      }
    }
  },
};
</script>
