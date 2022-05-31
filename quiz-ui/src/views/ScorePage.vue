<template>
<p>score : {{ score }}</p>
<div v-for="(participation, index) in leaderBoard">
  <p>{{ index+1 }} : {{ participation.playerName }} / {{ participation.score }}</p>
</div>
</template>

<script>
import quizApiService from '../services/quizApiService';
import localStorageService from '../services/LocalStorageService';
export default {
  name: "ScorePage",
  data() {
    return {
      playerName : '',
      leaderBoard : [],
      playerScore : 0
    };
  },
  async created() {
    this.playerName = localStorageService.getPlayerName();
    this.playerScore = localStorageService.getParticipationScore();
    quizApiService.getQuizInfo().then(response => {
      console.log(response);
      this.leaderBoard = response.data.scores;
    });
		console.log("Score Page of" + this.playerName + " / his score is :" + this.playerScore);
  }
};
</script>

<style scoped>
</style>