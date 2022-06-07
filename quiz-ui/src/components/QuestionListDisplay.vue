<template>
  <button class="btn btn-primary my-2" @click="addQuestion()">Ajouter une question</button>
  <table class="table table-bordered text-light text-center">
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
          <button class="btn btn-primary" @click="editQuestion(question.position)">Edit</button>
          <button class="btn btn-danger" @click="deleteQuestion(question.position)">Delete</button>
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