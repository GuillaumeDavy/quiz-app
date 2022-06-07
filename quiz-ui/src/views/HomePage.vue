<template>
  <div class="wrapper">

    <div class="container-xl container mt-5 bg-dark text-light p-3 rounded-2">
      <div class="center text-center">
        <div class="stage">
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
          <div class="layer"></div>
        </div>
      <div class="mt-5">
        <div v-if="registeredScores.scores.length > 0" class="leaderboard px-4 justify-content-center">
          <i class="d-inline fa fa-trophy fa-3x" aria-hidden="true"></i><p class="d-inline text-uppercase fs-2"> Leaderboard </p><i class="d-inline fa fa-trophy fa-3x" aria-hidden="true"></i>
          <table class="table table-hover table-responsive  text-center">
            <thead>
              <tr class="">
                <th class="table-light col-4">Position</th>
                <th class="table-light col-4">Nom du joueur</th>
                <th class="table-light col-4">Score</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(scoreEntry, index) in registeredScores.scores" v-bind:key="scoreEntry.date">
                <td class="table-light">{{ index+1 }}</td>
                <td class="table-light text-center">{{ scoreEntry.playerName }}</td>
                <td class="table-light">{{ scoreEntry.score }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <router-link to="/start-new-quiz-page" class="btn btn-danger">Démarrer le quiz !</router-link>
      </div>
    </div>
  </div>
        </div>
</template>

<script>
import quizApiService from "@/services/quizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores :[],
    };
  },
  async created() {
    quizApiService.getQuizInfo().then(response => {
      this.registeredScores = response.data;
      console.log(this.registeredScores.scores);
    });
		
  }
};

</script>

<style scoped>
@import url("//fonts.googleapis.com/css?family=Pacifico&text=Quiz-App");

.center{
  margin: auto;
  width: 100%;
}


.container-bg{
  background-color: #3a3a3a;
  max-width: 450px;
  padding: 20px;
  border-radius: 5px;
  /* add border shadow to this element */
  box-shadow: 0px 0px 20px 1px;

}

.stage {
  height: 200px;
  width: 500px;
  margin: auto;
  position: relative;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  perspective: 9999px;
  transform-style: preserve-3d;
}

.layer {
  width: 100%;
  height: 100%;
  position: absolute;
  transform-style: preserve-3d;
  animation: ಠ_ಠ 5s infinite alternate ease-in-out -7.5s;
  animation-fill-mode: forwards;
  transform: rotateY(40deg) rotateX(33deg) translateZ(0);
}

.layer:after {
  font: 150px/0.65 "Pacifico";
  content: "Quiz-App!";
  white-space: pre;
  text-align: center;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 50px;
  margin: 0 -300px;
  color: rgba(212, 10, 168, 0.829);
  letter-spacing: -2px;
  text-shadow: 4px 0 10px rgba(0, 0, 0, 0.13);
}

.layer:nth-child(1):after {
  transform: translateZ(0px);
}

.layer:nth-child(2):after {
  transform: translateZ(-1.5px);
}

.layer:nth-child(3):after {
  transform: translateZ(-3px);
}

.layer:nth-child(4):after {
  transform: translateZ(-4.5px);
}

.layer:nth-child(5):after {
  transform: translateZ(-6px);
}

.layer:nth-child(6):after {
  transform: translateZ(-7.5px);
}

.layer:nth-child(7):after {
  transform: translateZ(-9px);
}

.layer:nth-child(8):after {
  transform: translateZ(-10.5px);
}

.layer:nth-child(9):after {
  transform: translateZ(-12px);
}

.layer:nth-child(10):after {
  transform: translateZ(-13.5px);
}

.layer:nth-child(11):after {
  transform: translateZ(-15px);
}

.layer:nth-child(12):after {
  transform: translateZ(-16.5px);
}

.layer:nth-child(13):after {
  transform: translateZ(-18px);
}

.layer:nth-child(14):after {
  transform: translateZ(-19.5px);
}

.layer:nth-child(15):after {
  transform: translateZ(-21px);
}

.layer:nth-child(16):after {
  transform: translateZ(-22.5px);
}

.layer:nth-child(17):after {
  transform: translateZ(-24px);
}

.layer:nth-child(18):after {
  transform: translateZ(-25.5px);
}

.layer:nth-child(19):after {
  transform: translateZ(-27px);
}

.layer:nth-child(20):after {
  transform: translateZ(-28.5px);
}

.layer:nth-child(n+10):after {
  -webkit-text-stroke: 3px rgba(0, 0, 0, 0.25);
}

.layer:nth-child(n+11):after {
  -webkit-text-stroke: 15px dodgerblue;
  text-shadow: 6px 0 6px #00366b, 5px 5px 5px #002951, 0 6px 6px #00366b;
}

.layer:nth-child(n+12):after {
  -webkit-text-stroke: 15px #0077ea;
}

.layer:last-child:after {
  -webkit-text-stroke: 17px rgba(0, 0, 0, 0.1);
}

.layer:first-child:after {
  color: rgb(255, 255, 255);
  text-shadow: none;
}

@keyframes ಠ_ಠ {
  100% {
    transform: rotateY(-40deg) rotateX(-43deg);
  }
}
</style>