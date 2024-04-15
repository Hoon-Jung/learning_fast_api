<script>
export default{
  data() {
    return {
      message: "",
    };
  },
  created() {
    fetch("http://localhost:8000/hello").then((response) => {
      response.json().then((json) => {
        this.message = json.message;
      });
    });
  },
  methods:{

  }
}


</script>

<template>
  <h1>{{ message }}</h1>
</template>
