<script>
export default{
  props: {
    post_id: {
      type: String,
      required: true
    }
  },
  data() {
    return{
      post: {},
      content: ""
    }
  },
  created() {
    this.getPost()
  },
  methods: {
    getPost(){
      fetch(`http://localhost:8000/api/post/detail/${this.post_id}`).then((response) => {
        response.json().then((json) => {
            this.post = json;
            });
        });
    },
    addReply(event){
      event.preventDefault();

      let options={
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: this.content })
      }

      fetch(`http://localhost:8000/api/reply/add/${this.post_id}`, options).then((response) => {
        console.log(response);
        this.getPost();
      }).catch((error) => {
        console.log("Error:", error);
      })
    }
  },
};
</script>

<template>
  <h1> {{ this.post.subject }}</h1>
  <div> {{ this.post.content }}</div>
  <ul>
    <li v-for="comment in post.replies" :key="comment.id">
      {{ comment.content }}
    </li>
  </ul>
  <form @submit.prevent="addReply">
    <textarea rows="15" v-model="content"></textarea>
    <input type="submit" value="Add Comment" />
  </form>
</template>