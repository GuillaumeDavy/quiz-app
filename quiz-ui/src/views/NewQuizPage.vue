<template>
<div class="container-bg container mt-5 bg-dark text-light">
    <div class="center text-center">
      <h1 class="px-4">Nouvelle partie</h1>
      <div class="p-4 ">
        <div class="form-group col-6 form-center">
          <label for="exampleInputEmail1" class="pb-2" >Saisissez votre nom</label>
          <input type="text" v-model="username" placeholder="Username" class="form-control"/>
        </div>
        <div class="pt-4">
          <button v-on:click="launchNewQuiz" class="btn btn-danger">Start Quiz</button>
        </div>
      </div>
    </div>
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

<style>
.form-center{
  margin: auto;
}

.container-bg{
  background-color: #3a3a3a;
  max-width: 830px;
  padding: 20px;
  border-radius: 5px;
  /* add border shadow to this element */
  box-shadow: 0px 0px 20px 1px;

}
</style>