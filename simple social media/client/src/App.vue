<template>
  <navigation_bar />
  <router-view />
</template>

<script>
import navigation_bar from "@/components/navigation_bar.vue";
export default {
  name: "App",
  components: {
    navigation_bar,
  },
};
</script>