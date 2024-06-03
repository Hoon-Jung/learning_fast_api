<template>
    <div>
      <div v-if="typeof error.detail === 'string'">
        <div class="alert alert-danger" role="alert">
          {{ error.detail }}
        </div>
      </div>
      <div
        v-else-if="typeof error.detail === 'object' && error.detail.length > 0"
      >
        <div class="alert alert-danger" role="alert">
          <div v-for="(err, i) in error.detail" :key="i">
            <strong>{{ err.loc[1] }}</strong> : {{ err.msg }}
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      error: {
        type: Object,
        default: () => ({}),
      },
    },
  };
  </script>