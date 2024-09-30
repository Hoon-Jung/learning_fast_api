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

        <div class="my-3" v-if="postVoted">
          <button class="btn btn-success active" data-bs-toggle="button" aria-pressed="true" @click="likePost(post.id)">
            <solid_thumbs_up class="icon"></solid_thumbs_up> {{ post.voter.length }}
           </button>
        </div>
        <div class="my-3" v-else>
          <button class="btn btn-success" data-bs-toggle="button" @click="likePost(post.id)">
            <outline_thumbs_up class="icon"></outline_thumbs_up> {{ post.voter.length }}
           </button>
        </div>

        <div class="my-3" v-if="post.user && $store.state.username === post.user.username">
        <router-link :to=" '/update_post/' + post.id " class="btn btn-sm btn-outline-secondary">Edit</router-link>
        <button class="btn btn-sm btn-outline-danger" @click="deletePost(post.id)">Delete</button>
        </div>

      </div>
    </div>
    <div class="dropdown">
      <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
        Filter by
      </button>
      <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
        <li><a class="dropdown-item" href="#" @click="setSort('voter_count', true)">Most Likes</a></li>
        <li><a class="dropdown-item" href="#" @click="setSort('voter_count', false)">Least Likes</a></li>
        <li><a class="dropdown-item" href="#" @click="setSort('created_at', false)" >Oldest</a></li>
        <li><a class="dropdown-item" href="#" @click="setSort('created_at', true)" >Newest</a></li>
      </ul>
    </div>
        




        <h5 class="border-bottom my-3 py-2">
          {{ post.replies?.length }} replies
        </h5>
        <div class="card my-3" v-for="reply in replies" :key="reply.id">
          <div class="card-body">
            <div class="card-text" style="white-space: pre-line">
              {{ reply.content }}
            </div>
            <div class="d-flex justify-content-end">
              <div class="badge bg-light text-dark p-2">
                @{{ reply.user.username }} | {{ formatDate(reply.created_at) }}
              </div>
            </div>
            <div class="my-3" v-if="reply.user && reply.voter.some(voter => voter.username === $store.state.username)">
              <button class="btn btn-success active" @click="likeReply(reply.id)">Likes 
                <span class="badge rounded-pill bg-success">{{ reply.voter.length }}</span>
              </button>
            </div>
            <div class="my-3" v-else>
              <button class="btn btn-success" @click="likeReply(reply.id)">Likes 
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
    <ul class="pagination justify-content-center">
      <li class="page-item" :class="{ disabled: page <= 0 }">
        <button class="page-link" @click="$store.commit('setCommentPage', 0);">First</button>
      </li>
      <li class="page-item" :class="{ disabled: page <= 0 }">
        <button class="page-link" @click="$store.commit('setCommentPage', page-1);">Back</button>
      </li>
      <template
        v-for="(_, loop_page) in Array.from({ length: totalPage })"
        :key="loop_page"
      >
        <li
          class="page-item"
          v-if="loop_page >= page - 5 && loop_page <= page + 5"
          :class="{ active: loop_page === page }"
        >
          <button class="page-link" @click="$store.commit('setCommentPage', loop_page);">
            {{ loop_page + 1 }}
          </button>
        </li>
      </template>
      <li class="page-item" :class="{ disabled: page >= totalPage - 1 }">
        <button class="page-link" @click="$store.commit('setCommentPage', page+1);">Next</button>
      </li>
      <li class="page-item" :class="{ disabled: page >= totalPage - 1 }">
        <button class="page-link" @click="$store.commit('setCommentPage', totalPage-1);">Last</button>
      </li>
    </ul>
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
// import marked from "marked";
import fastapi from '../../lib/api';
import error_component from "../components/error_component.vue";
import {HandThumbUpIcon as OutlineThumbsUp} from "@heroicons/vue/24/outline";
import {HandThumbUpIcon as SolidThumbsUp} from "@heroicons/vue/24/solid";

export default{
  components: {
    error_component,
    outline_thumbs_up: OutlineThumbsUp,
    solid_thumbs_up: SolidThumbsUp,
  },
  props: {
    post_id: {
      type: String,
      required: true
    },
  },
  watch: {
    page(){
      this.getReplies();
    },
    sort_by(){
      this.getReplies();
    },
    desc(){
      this.getReplies();
    },
  },
  computed: {
    sort_by(){
      return this.$store.state.sortby;
    },
    desc(){
      return this.$store.state.desc;
    },
    postVoted(){
      const username = this.$store.state.username;
      return this.post.voter.some((user) => user.username === username);
    },
    page(){
      return this.$store.state.commentPage;
    },
    totalPage() {
      return Math.ceil(this.total / this.p_size)
    },
  },
  data() {
    return{
      post: { voter: {} },
      content: "",
      error: { detail:[] },
      p_size: 10,
      total: 0,
      replies: [],
    }
  },
  created() {
    this.getPost();
    this.getReplies();
  },
  methods: {
    replyVoted(rep){
      const username = this.$store.state.username;
      return rep.voter.some((user) => user.username === username);
    },
    setSort(sortby, desc){
      this.$store.commit('setSortBy', sortby);
      this.$store.commit('setDesc', desc);
    },
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
        this.getReplies();
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
    getReplies() {
      let params = {
        page: this.page,
        page_size: this.p_size,
        post_id: this.post_id,
        sort_by: this.sort_by,
        desc: this.desc,
      }
      fastapi("get", "/api/reply/list", params, (json) => {
        this.replies = json.reply_list;
        this.total = json.total;
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


<style>
.icon{
  width: 18px;
  height: 18px;
}
</style>