<template>
  <div class="container my-3">
    <table class="table">
      <thead>
        <tr class="table-dark">
          <th>Post Number</th>
          <th>User</th>
          <th>Title</th>
          <th>Replies</th>
          <th>Posted at</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(post, i) in allposts" :key="post.id">
          <td>{{ total - (page * this.p_size) - i }}</td>
          <td v-if="post.user">@{{ post.user.username }}</td>
          <td v-else>N/A</td>
          <td>
            <router-link :to="'/body/' + post.id">{{
              post.subject
            }}</router-link>
          </td>
          <td>
            <span class="mx-1"> {{ post.replies?.length }} replies</span>
          </td>
          <td>{{ formatDate(post.created_at) }}</td>
        </tr>
      </tbody>
    </table>

    <ul class="pagination justify-content-center">
      <li class="page-item" :class="{ disabled: page <= 0 }">
        <button class="page-link" @click="getPosts(0)">First</button>
      </li>
      <li class="page-item" :class="{ disabled: page <= 0 }">
        <button class="page-link" @click="getPosts(page - 1)">Back</button>
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
          <button class="page-link" @click="getPosts(loop_page)">
            {{ loop_page + 1 }}
          </button>
        </li>
      </template>
      <li class="page-item" :class="{ disabled: page >= totalPage - 1 }">
        <button class="page-link" @click="getPosts(page + 1)">Next</button>
      </li>
      <li class="page-item" :class="{ disabled: page >= totalPage - 1 }">
        <button class="page-link" @click="getPosts(totalPage-1)">Last</button>
      </li>
    </ul>
    
    <div class="d-flex justify-content-start" v-if="is_logged_in">
      <router-link to="/post-add" class="btn btn-primary"
        >Post</router-link>
    </div>
    <div class="d-flex justify-content-start" v-else>
      <div class="btn btn-primary">Log in to Post</div>
    </div>
  </div>
</template>


<!-- <template>
  <ul>
    <li v-for="post in allposts" :key="post.id">
        <router-link :to="'/body/' + post.id">{{ post.subject }}</router-link>
    </li>
  </ul>
</template> -->


<script>
import fastapi from '../../lib/api';
import moment from "moment";

export default{
  data() {
    return {
        allposts: [],
        p_size: 10,
        total: 0,
    }
  },
  computed: {
    page(){
      return this.$store.state.page;
    },
    totalPage() {
      return Math.ceil(this.total / this.p_size)
    },
    is_logged_in(){
      return this.$store.state.is_login;
    },
  },
  created() {
    this.getPosts(this.$store.state.page);
  },
  methods: {
    formatDate(dt){
      return moment(dt).startOf("hour").fromNow();
    },
    getPosts(p) {
      let params = {
        page: p,
        page_size: this.p_size,
      }
      fastapi("get", "/api/post/list", params, (json) => {
        this.allposts = json.posts;
        this.total = json.total;
        this.$store.dispatch("setPage", p);
      });
    },
  },
};


</script>