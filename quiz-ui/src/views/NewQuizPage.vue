<template>
  <h1 class="px-4">New Quiz Page</h1>
  <div class="p-4">
    <div class="form-group ">
      <label for="exampleInputEmail1" >Saisissez votre nom</label>
      <input type="text" v-model="username" placeholder="Username" class="form-control"/>
    </div>
    <button v-on:click="launchNewQuiz" class="btn btn-outline-danger mt-1">Start Quiz</button>
  </div>

</template>

<script>
import localStorageService from "@/services/LocalStorageService";
export default {
  
  name: "NewQuizPage",
  data() {
    return {
      username: '',
    };
  },
  methods: {
    launchNewQuiz() {
      localStorageService.savePlayerName(this.username);
      this.$router.push('/questionsManager');
    },
  },
  async created() {
		console.log("Composant New quiz page 'created'");
  }
};
</script>