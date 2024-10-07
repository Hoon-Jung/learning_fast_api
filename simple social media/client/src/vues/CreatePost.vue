<template>
    <div class="container my-3">
      <h4>Create a Post</h4>
      <error_component :error="error" />
      <form @submit.prevent="createPost">
        <div class="form-group">
          <div class="col-md-2">
            <select class="form-control" id="category" v-model="selectedCategory">
              <option disabled value="">Select a Category ></option>
              <option v-for="(category_name, category_id) in categoryOptions" :key="category_id" :value="category_name">
                {{ category_name }}
              </option>
            </select>
          </div>
        </div>
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
      selectedCategory: "",
      categories: {
        "Humor": 1,
        "Technology": 2,
        "Movies & TV": 3,
        "Video Games": 4,
        "Fashion": 5,
      },
      categoryMapping: {
        1: "Humor",
        2: "Technology",
        3: "Movies & TV",
        4: "Video Games",
        5: "Fashion",
      },
    }
  },
  computed: {
    categoryOptions(){
      return Object.keys(this.categories);
    }
  },
  created() {
    const urlParams = new URLSearchParams(window.location.search);
    const category_id = urlParams.get("category_id");
    if(category_id) this.selectedCategory = this.categoryMapping[category_id];
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
