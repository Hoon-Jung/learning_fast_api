<template>
  <navigation_bar />
  <side_bar />
  <router-view />
</template>

<script>
import navigation_bar from "@/components/navigation_bar.vue";
import side_bar from "@/components/side_bar.vue";
export default {
  name: "App",
  components: {
    navigation_bar,
    side_bar,
  },
};
</script>