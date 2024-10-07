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
      categoryid: 0,
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
  mounted() {
    let url = "/api/post/detail/" + this.post_id;
    fastapi("get", url, {}, (json) => {
        this.subject = json.subject;
        this.content = json.content;
        this.selectedCategory = json.category.subject;
    });
  },
  created() {
    // if(categoryid) this.selectedCategory = this.categoryMapping[categoryid];
  },
  methods: {
    updatePost(){
      let params={
        subject: this.subject,
        content: this.content,
        post_id: this.post_id,
        category_id: this.categories[this.selectedCategory],
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
