<template>
<div class="container-xl container mt-5 bg-dark text-light p-3 rounded-2 text-center h3">
  <h1 class="page-title">Résultat du Quiz !</h1>
  <Leaderboard :registeredScores="leaderBoard"></Leaderboard>
  <div class="d-flex justify-content-center">
    <router-link to="/start-new-quiz-page" class="btn btn-danger">Nouvelle partie</router-link>
  </div>
</div>
</template>

<script>
import quizApiService from '../services/quizApiService';
import localStorageService from '../services/LocalStorageService';
import Leaderboard from "../components/Leaderboard.vue";

export default {
  name: "ScorePage",
  data() {
    return {
      currentPlayerName : '',
      leaderBoard : {},
      playerScore : 0,
    };
  },
  components: {
    Leaderboard
  },
  async created() {
    this.currentPlayerName = localStorageService.getPlayerName();
    this.playerScore = localStorageService.getParticipationScore();
    quizApiService.getQuizInfo().then(response => {
      console.log(response);
      this.leaderBoard = response.data.scores;
    });
		console.log("Score Page of " + this.currentPlayerName + " / his score is :" + this.playerScore);
  }
};
</script>

<style scoped>




</style>