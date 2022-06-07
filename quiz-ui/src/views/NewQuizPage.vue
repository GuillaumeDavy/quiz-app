<template>
<div class="container-bg container mt-5 bg-dark text-light">
    <div class="center text-center">
      <h1 class="px-4 page-title">Nouvelle partie</h1>
      <div class="p-4 ">
        <div class="form-group col-6 form-center">
          <label class="pb-2 fs-4" >Saisissez votre nom</label>
          <input type="text" v-model="username" placeholder="Username" class="form-control"/>
        </div>
        <div class="pt-4">
          <div class="alert alert-danger" v-if="error">{{ error }}</div>
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
      error: '',
    };
  },
  methods: {
    launchNewQuiz() {
      if(this.username.length < 5) {
        this.error = 'Votre nom doit faire au moins 5 caractères';
      }else{
        localStorageService.savePlayerName(this.username);
        this.$router.push('/questionsManager');
      }
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
  box-shadow: 0px 0px 10px 1px;

}

.page-title {
	text-transform: uppercase;
	background: linear-gradient(to right, #0077ff 0%, #e40cc7 100%);
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
  font-size: 4vw;
}
</style>