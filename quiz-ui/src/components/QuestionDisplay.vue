<template>
  <div class="my-2">
    {{ question.text }}
  </div>
  <img v-if="question.image" :src="question.image" height="300" width="400" />
  <div class="row question-container mt-4">

    <div class="col-6 p-2" v-for="(answer, index) in question.possibleAnswers">
    
    <button class="question-button" @click="$emit('answer-selected', index+1)">{{ answer.text }}</button>
  </div>
  </div>
  
</template>

<script>
export default {
  name: "QuestionDisplay",
  data() {
    return {
    };
  },
  methods: {},
  props: {
    question: {
      type: Object
    }
  },
  emits: ["answer-selected"],
  async created() {
		console.log("Question Display");
  }
};
</script>

<style>
.question-container{
  width: 80%;
  margin: auto;
}

.question-button{
  background-color: black;
  color: white;
  min-width: 100%;
  max-width: 100%;
  min-height: 90px;
  max-height: 90px;
  border-radius: 5px;
  padding: 10px;
  /* blue border color */
  border: 1px solid #0099ff;
  /* add border shadow to this element */
  flex: 1; /* additionally, equal width */
  
}

.question-button:hover{
  background-color:orange;
  color: rgb(0, 0, 0);
}
</style>