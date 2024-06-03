<template>
  <div class="container my-3">
    <table class="table">
      <thead>
        <tr class="table-dark">
          <th>Post Number</th>
          <th>Title</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in allposts" :key="post.id">
          <td>{{ post.id }}</td>
          <td>
            <router-link :to="'/body/' + post.id">{{
              post.subject
            }}</router-link>
          </td>
          <td>{{ post.create_date }}</td>
        </tr>
      </tbody>
    </table>
    <!-- <div class="d-flex justify-content-start">
      <router-link to="/post-add" class="btn btn-primary"
        >질문 등록하기</router-link
      >
    </div> -->
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
export default{
  data() {
    return {
        allposts: [],
    }
  },
  created() {
    this.getPosts();
  },
  methods: {
    getPosts() {
      fastapi("get", "/api/post/list", {}, (json) => {
        this.allposts = json;
      });
    },
  },
};
</script>