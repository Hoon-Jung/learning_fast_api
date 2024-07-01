<template>
  <div class="container">
    <h5 class="my-3 border-bottom pb-2">Sign up</h5>
    <ErrorComponent :error="error" />
    <form @submit.prevent="createUser">
      <div class="mb-3">
        <label for="username">Username</label>
        <input
          type="text"
          class="form-control"
          id="username"
          v-model="username"
        />
      </div>
      <div class="mb-3">
        <label for="password1">Password</label>
        <input
          type="password"
          class="form-control"
          id="password1"
          v-model="password1"
        />
      </div>
      <div class="mb-3">
        <label for="password2">Confirm password</label>
        <input
          type="password"
          class="form-control"
          id="password2"
          v-model="password2"
        />
      </div>
      <div class="mb-3">
        <label for="email">Email</label>
        <input type="text" class="form-control" id="email" v-model="email" />
      </div>
      <button type="submit" class="btn btn-primary">Sign up</button>
    </form>
  </div>
</template>


<script>
import fastapi from '../../lib/api';
import ErrorComponent from "@/components/error_component.vue";

export default {
  components: {
    ErrorComponent,
  },
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
      error: { detail: [] }
    };
  },
  methods: {
    createUser(){
      let params={
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,
      };
      fastapi("post", `/api/user/create`, params, () => {
        this.$router.push("/");
      },
      (err) => {
        this.error = err; 
      });

    }
  },
}
</script>
