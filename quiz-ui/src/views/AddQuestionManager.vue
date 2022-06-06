<template>
  <div class="container-xl container mt-5 bg-dark text-light p-3 rounded-2">
    <div class="form">
      <div class="form-group">
        <label for="title">Titre de la question</label>
        <input type="text" class="form-control" id="title" placeholder="Ici le titre de la question" v-model="form.title"> 
        <label for="text">Texte de la question</label>
        <input type="text" class="form-control" id="text" placeholder="Ici le texte de la question" v-model="form.text"> 
        <label for="position">Position de la question</label>
        <input type="number" class="form-control" id="position" placeholder="Position de la question" v-model="form.position"> 
        <label for="image">Image de la question</label>
        <ImageUpload @file-change="imageFileChangedHandler" />
        <img v-if="form.image" :src="form.image" height="300" width="400" /><br>

        <label for="questionAnswers">Réponses de la question</label> 
        <div v-for="(answer, index) in form.possibleAnswers">
          <input type="text" class="form-control" id="questionAnswers" placeholder="Ici la réponse" v-model="answer.text">
          <input type="radio" name="checkboxAnswerCorrect" v-model="correctAnswer" :value="index">
        </div>
      </div>
    </div>
     <div class="alert alert-danger" v-if="error">{{ error }}</div>
     <button v-on:click="addQuestion()" class="btn btn-outline-danger mt-1">Insérer la question</button>
  </div>
</template>

<script>
import ImageUpload from '../components/ImageUpload.vue';
import quizApiService from '../services/quizApiService';
import router from '../router';
export default {
  name: "AddQuestionManager",
  data() {
    return {
      error: '',
      correctAnswer : 0,
      form:{
        text: '',
        title: '',
        image: '',
        position: '',
        possibleAnswers: [
          {
            isCorrect: false,
            question:0,
            text: '',
          },
          {
            isCorrect: false,
            question:0,
            text: '',
          },
          {
            isCorrect: false,
            question:0,
            text: '',
          },
          {
            isCorrect: false,
            question:0,
            text: '',
          },
        ],
      }
    };
  },
  components: {
    ImageUpload
  },
  watch: {
    
  },
  methods:{
    imageFileChangedHandler(b64String) {
      this.form.image = b64String;
    },
    addQuestion() {
      var counterValidAnswers = 0;
      if(this.form.text.length > 0 && this.form.title.length > 0 
        && this.form.position > 0 && this.form.image.length > 0) {
          this.form.possibleAnswers.forEach(answer => {
            if(answer.text.length > 0) {
              counterValidAnswers++;
            }
          });
        if(counterValidAnswers > 3){
          console.log(this.form)
          var index = 0;
          this.form.possibleAnswers.forEach(validAnswer => {
            validAnswer.question = this.form.position;
            if(index == this.correctAnswer){
              validAnswer.isCorrect = true;
            }else{
              validAnswer.isCorrect = false;
            }
            index++;
          });
          quizApiService.addQuestion(this.form, localStorage.getItem('token'))
            .then(() => {
              router.push('/admin');
            })
        }else{
          this.error = "Veuillez remplir toutes les réponses";
        }
      }else{
        this.error = "Veuillez remplir tous les champs";
      }
    }
  },
  async created() {
  }
};
</script>

<style scoped>
</style>