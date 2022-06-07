<template>
<div class="container-xl container mt-5 bg-dark text-light p-3 rounded-2">
  <div v-for="(participation, index) in leaderBoard">
    <p v-if="participation.playerName === currentPlayerName" class="fs-4">Vous : {{ participation.playerName }}</p>
    <p v-else>{{ index+1 }} : {{ participation.playerName }} / {{ participation.score }}</p>
  </div>
</div>
</template>

<script>
import quizApiService from '../services/quizApiService';
import localStorageService from '../services/LocalStorageService';
export default {
  name: "ScorePage",
  data() {
    return {
      currentPlayerName : '',
      leaderBoard : {},
      playerScore : 0,
    };
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