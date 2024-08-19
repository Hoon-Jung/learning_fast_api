<template>
    <div class="container">
      <error_component :error="error" />
      <h5 class="my-3 border-bottom pb-2">Edit Comment</h5>
      <form @submit.prevent="updateReply" class="my-3">
        <div class="mb-3">
          <label for="content">Content</label>
          <textarea class="form-control" rows="10" v-model="content"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Save Changes</button>
      </form>
    </div>
  </template>

<script>
import fastapi from '../../lib/api';
import error_component from "../components/error_component.vue";
export default {
  components: {
    error_component,
  },
  props: {
    reply_id: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      error: { detail: [] },
      post_id: 0,
      content: "",
    };
  },
  mounted() {
    fastapi("get", "/api/reply/detail/" + this.reply_id, {}, (json) => {
      console.log(json);
      this.post_id = json.post_id;
      this.content = json.content;
    });
  },
  methods: {
    updateReply() {
      let url = "/api/reply/update";
      let params = {
        id: this.reply_id,
        content: this.content,
      };
      fastapi(
        "put",
        url,
        params,
        () => {
          this.$router.push("/body/" + this.post_id);
        },
        (err_json) => {
          this.error = err_json;
        }
      );
    },
  },
};
</script>