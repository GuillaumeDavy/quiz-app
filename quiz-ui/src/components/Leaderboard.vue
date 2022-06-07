<template>
  <div class="leaderboard px-4 justify-content-center">
    <i class="d-inline fa fa-trophy fa-3x" aria-hidden="true"></i><p class="d-inline text-uppercase fs-2"> Leaderboard </p><i class="d-inline fa fa-trophy fa-3x" aria-hidden="true"></i>
    <table class="table table-hover table-responsive table-dark text-center">
    <thead>
        <tr class="">
        <th class=" col-4">Position</th>
        <th class=" col-4">Nom du joueur</th>
        <th class=" col-4">Score</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(scoreEntry, index) in registeredScores" v-bind:key="scoreEntry.date">
        <td>{{ index+1 }}</td>
        <td class="text-center">{{ scoreEntry.playerName }}</td>
        <td>{{ scoreEntry.score }}</td>
        </tr>
    </tbody>
    </table>
</div>
  
</template>

<script>
export default {
  name: "Leaderboard",
  data() {
    return {
        registeredScores :[],
    };
  },
  methods: {},
  props: {
    registeredScores: {
      type: Array,
      required: true,
    },
  },
  async created() {
		console.log("Leaderboard");
  }
};
</script>

<style>
</style>