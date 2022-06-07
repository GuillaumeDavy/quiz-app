<template>
  <button class="btn btn-primary my-3" @click="addQuestion()"> <b class="h5">+</b> Ajouter une question</button>
  <table class="table table-bordered text-light text-center">
    <thead>
      <tr>
        <th scope="col">Position</th>
        <th scope="col">Title</th>
        <th scope="col">Text</th>
        <th scope="col">Image</th>
        <th scope="col">Réponses</th>
        <th scope="col">Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr class="align-middle" v-for="question in questionList">
        <th scope="row align-middle">{{ question.position }}</th>
        <td>{{ question.title }}</td>
        <td>{{ question.text }}</td>
        <td>
          <img v-if="question.image" :src="question.image" width="150" height="100"/>
        </td>
        <div v-for="(answer, index) in question.possibleAnswers" class="answers row align-middle">
          <div class="col-10">
            {{index+1}} - {{ answer.text }}
          </div>
          <div class="col-2">
            <div v-if="answer.isCorrect" class="text-success">
              <i class="fa fa-check" aria-hidden="true"></i>
            </div>
            <div v-if="!answer.isCorrect" class="text-danger">
              <i class="fa fa-times" aria-hidden="true"></i>
            </div>
          </div>
        </div>
        <td>
          <div class="col-12 p-3">
            <button class="btn btn-primary" @click="editQuestion(question.position)">Edit</button>
          </div>
          <div class="col-12 p-3">
            <button class="btn btn-danger" @click="deleteQuestion(question.position)">Delete</button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import quizApiService from '../services/quizApiService';
import router from '../router';
export default {
  name: "QuestionListDisplay",
  data() {
    return {
      questionList : [],
    };
  },
  components: {
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
      quizApiService.deleteQuestion(position, localStorage.getItem('token'))
        .then(() => {
          this.getAllQuestions();
        });
    },
    addQuestion() {
      router.push('/question/add');
    },
    editQuestion(questionPosition) {
      router.push(
        {
          path: '/edit-question/',
          query: {
            id: questionPosition
          }
        }
      );
    },
    
  },
  async created() {
    this.getAllQuestions();
		console.log("Question List Display");
  }
};

</script>

<style>
.answers{
  line-height: 1;
  font-size: 0.8rem;
}
</style>