<template>
  <button class="btn btn-primary my-2" @click="addQuestion()">Add Question</button>
  <QuestionModal :question="null"
    v-show="displayEmptyModal"
    @close="displayEmptyModal = false"
  />
  <table class="table table-bordered">
    <thead>
      <tr>
        <th scope="col">Position</th>
        <th scope="col">Title</th>
        <th scope="col">Text</th>
        <th scope="col">Image</th>
        <th scope="col">Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="question in questionList">
        <th scope="row">{{ question.position }}</th>
        <td>{{ question.title }}</td>
        <td>{{ question.text }}</td>
        <td><img v-if="question.image" :src="question.image" width="300" height="200"/></td>
        <td>
          <button class="btn btn-primary" @click="editQuestion(question);$emit('edit')">Edit</button>
          <button class="btn btn-danger" @click="deleteQuestion(question.position)">Delete</button>
        </td>
      </tr>
    </tbody>
  </table>
  <QuestionModal :question=wantedQuestion
    v-show="displayQuestionModal"
    @close="displayQuestionModal = false"
  />
</template>

<script>
import QuestionModal from '../components/QuestionModal.vue';
import quizApiService from '../services/quizApiService';
export default {
  name: "QuestionListDisplay",
  data() {
    return {
      wantedQuestion : null,
      questionList : [],
      displayEmptyModal : false,
      displayQuestionModal : false,
    };
  },
  components: {
    QuestionModal
  },
  methods: {
    getAllQuestions() {
      quizApiService.getQuestions()
        .then(response => {
          this.questionList = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    deleteQuestion(position) {
      quizApiService.deleteQuestion(position)
        .then(() => {
          this.getAllQuestions();
        });
    },
    addQuestion() {
      this.displayEmptyModal = true;
    },
    editQuestion(question) {
      this.wantedQuestion = question;
      this.displayQuestionModal = true;
    },
  },
  async created() {
    this.getAllQuestions();
		console.log("Question List Display");
  }
};
</script>