<template>
    <div class="container">
      <h5 class="my-3 border-bottom pb-2">Login</h5>
      <error_component :error="error" />
      <form @submit.prevent="loginUser">
        <div class="mb-3">
          <label for="username">Username</label>
          <input type="text" class="form-control" id="username" v-model="login_username">
        </div>
        <div class="mb-3">
          <label for="password">Password</label>
          <input type="password" class="form-control" id="password" v-model="login_password">
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
      </form>
    </div>
  </template>

<script>
import fastapi from "../../lib/api"
import error_component from "../components/error_component.vue"
export default {
  components: {
    error_component
  },
  data() {
    return {
        error: { details: {}},
        login_password: "",
        login_username: "",
    }
  },
  methods: {
    loginUser() {
        let params = {
            username: this.login_username,
            password: this.login_password
        }
        fastapi("login", `/api/user/login`, params, (json) => {
            this.$store.dispatch("setAccessToken", json.access_token);
            this.$store.dispatch("setUsername", json.username);
            this.$store.dispatch("setIsLogin", true);
            this.$router.push("/");
        },
        (err) => {
            this.error = err; 
        });

    }
  }
}
</script>