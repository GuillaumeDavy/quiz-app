<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
</template>

<script>
import QuestionDisplay from "@/components/QuestionDisplay.vue";
import quizApiService from "../services/quizApiService";
import localStorageService from "../services/LocalStorageService";
import router from "../router";
export default {
  name: "QuestionsManager",
  data() {
    return {
      currentQuestionPosition: 1,
      totalNumberOfQuestion:0,
      currentQuestion:[],
      playerAnswers:[]
    };
  },
  methods: {
    loadQuestionByPosition(position) {
      quizApiService.getQuestion(position).then((question) => {
        this.currentQuestion = question.data;
      });
    },
    answerClickedHandler(answerId){
      console.log("Answer clicked: " + answerId);
      this.playerAnswers.push(answerId);
      console.log(this.playerAnswers);
      this.currentQuestionPosition++;
      if(this.currentQuestionPosition <= this.totalNumberOfQuestion){
        this.loadQuestionByPosition(this.currentQuestionPosition);
      }
      else{
        this.endQuiz()
      }
    }, 
    endQuiz(){
      quizApiService.submitParticipation(localStorageService.getPlayerName(), this.playerAnswers)
      .then((response) => {
        console.log(response);
        if(response.status === 200){
          localStorageService.saveParticipationScore(response.data.score);
          router.push("/score");
        }else{
          //toDo return error to user
        }
      });
    }
  },
  components: {
    QuestionDisplay
  },
  async created() {
    this.loadQuestionByPosition(1);

    await quizApiService.getQuizInfo().then(response => {
      this.totalNumberOfQuestion = response.data.size;
      localStorageService.saveQuestionSize(response.data.size);
    });
		console.log("Question Manager");
  }
};
</script>