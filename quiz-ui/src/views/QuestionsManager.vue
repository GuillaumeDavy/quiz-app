<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <button @click="loadQuestionByPosition(1)">Call question</button>
  <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
import QuestionDisplay from "@/components/QuestionDisplay.vue";
import quizApiService from "../services/quizApiService";
import localStorageService from "../services/LocalStorageService";
export default {
  name: "QuestionsManager",
  data() {
    return {
      currentQuestionPosition: 1,
      currentQuestion: {},
    };
  },
  methods: {
    loadQuestionByPosition(position) {
      quizApiService.getQuestion(position).then((question) => {
        console.log(question);
        this.currentQuestion = question;
      });
    },
  },
  components: {
    QuestionDisplay
  },
  async created() {
    quizApiService.getQuizInfo().then(response => {
      localStorageService.saveQuestionSize(response.data.size);
    });
		console.log("Question Manager");
  }
};
</script>