<template>
  <div class="container-xl container mt-5 bg-dark text-light">
    <div class="container p-4 rounded">
      <h1 class="page-title">ADMIN PAGE</h1>
      <QuestionListDisplay/>
    </div>
  </div>
</template>

<script>
import QuestionListDisplay from '../components/QuestionListDisplay.vue';
export default {
  name: "AdminManager",
  data() {
    return {
      
    };
  },
  components: {
    QuestionListDisplay
  },
  async created() {
  }
};
</script>

<style scoped>
</style>