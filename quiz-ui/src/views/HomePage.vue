<template>
  <h1>Home page Groupe des bg</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <router-link to="/start-new-quiz-page" class="btn btn-danger">Démarrer le quiz !</router-link>
</template>

<script>
import quizApiService from "@/services/quizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores :[],
    };
  },
  async created() {
    quizApiService.getQuizInfo().then(response => {
      this.registeredScores = response.data;
    });
		console.log("Composant Home page 'created'");
  }
};
</script>

<style scoped>
</style>