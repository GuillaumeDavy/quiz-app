<template>
  <img v-if="question.image" :src="question.image" />
  {{ question.position }}
  <a @click="$emit('answer-selected', 2)">La réponse D</a>
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