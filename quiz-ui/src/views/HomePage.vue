<template>
  <div class="wrapper">

    <div class="container-bg container mt-5 bg-dark text-light">
      <div class="center text-center">
        <h1>Quiz-App</h1>
      <div class="mt-5">
        <h4>JOUDIOUX Alexandre</h4>
        <h4>JOUEN Matthias</h4>
        <h4>DAVY Guillaume</h4>
        <div v-if="registeredScores.scores.length > 0" class="leaderboard">
          <p>Leaderboard</p>
          <div v-for="scoreEntry in registeredScores.scores" v-bind:key="scoreEntry.date">
          {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
          </div>
        </div>
        
        <router-link to="/start-new-quiz-page" class="btn btn-danger">Démarrer le quiz !</router-link>
      </div>
    </div>
  </div>
        </div>
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
      console.log(this.registeredScores.scores);
    });
		
  }
};
</script>

<style scoped>


.center{
  margin: auto;
  width: 100%;
}


.container-bg{
  background-color: #3a3a3a;
  max-width: 450px;
  padding: 20px;
  border-radius: 5px;
  /* add border shadow to this element */
  box-shadow: 0px 0px 20px 1px;

}
</style>