<template>
  <div class="container">
    <h1>ADMIN PAGE</h1>
    <QuestionListDisplay/>
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