<template>
  <div class="container-xl container mt-5 bg-dark text-light p-3 rounded-2">
    <div class="container">
      <h1>EDIT QUESTION PAGE</h1>
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
            <input :checked="index == correctAnswer" type="radio" name="checkboxAnswerCorrect" v-model="correctAnswer" :value="index">
          </div>
        </div>
        <button @click="editQuestion()">Valider</button>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from "../services/quizApiService";
import ImageUpload from "../components/ImageUpload.vue";
import router from "../router";
export default {
  name: "EditQuestionManager",
  data() {
    return {
      questionId: 0,
      question:{},
      image: '',
      correctAnswer: 0,
      test:0,
      form:{
        title: '',
        text: '',
        image: '',
        position: '',
        possibleAnswers: [
          {
            text: '',
            isCorrect: false,
            question:0,
            
            
          }
        ],
      }
    };
  },
  methods: {
    loadQuestionByPosition(position) {
      quizApiService.getQuestion(position).then((question) => {
        this.question = question.data;
        this.form.title = this.question.title;
        this.form.text = this.question.text;
        this.form.image = this.question.image;
        this.form.position = this.question.position;
        this.form.possibleAnswers = this.question.possibleAnswers;

        this.setCorrectAnswer(question.data);
      });
    },
    imageFileChangedHandler(b64String) {
      this.form.image = b64String;
    },
    setCorrectAnswer(question) {
      var correctIndexAnswer = 0;
      (question.possibleAnswers).forEach(answer => {
        if(answer.isCorrect == true){
          this.correctAnswer = correctIndexAnswer;
        }
        correctIndexAnswer++;
      });
    },
    editQuestion(){
      var correctIndexAnswer = 0;
      this.form.possibleAnswers.forEach(answer => {
        answer.question = this.form.position;
        if(correctIndexAnswer == this.correctAnswer){
          answer.isCorrect = true;
        }else{
          answer.isCorrect = false;
        }
        correctIndexAnswer++;
      });
      console.log(this.form);
      console.log(this.question.position);
      //si on a modifié la position de la question
      quizApiService.updateQuestion(this.form, this.question.position)
      router.push('/admin');
    }
  },
  components: {
    ImageUpload
},
  async created() {
		console.log("EDIT Question Manager");
    //get id from route
    this.questionId = this.$route.query.id;
    this.loadQuestionByPosition(this.questionId);
    
  }
};
</script>