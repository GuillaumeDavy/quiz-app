<template>
  {{ question.text }}
  <img v-if="question.image" :src="question.image" />
 
  <div v-for="(answer, index) in question.possibleAnswers">
    <button @click="$emit('answer-selected', index+1)">{{ answer.text }}</button>
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