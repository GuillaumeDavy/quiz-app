<template>
<div class="container-bg container mt-5 bg-dark text-light">
  <h1>LOGIN PAGE</h1>
  <div class="form-group">
      <label for="exampleInputEmail1" >Saisissez le mot de passe</label>
      <input type="password" v-model="password" placeholder="Password" class="form-control"/>
      <div class="alert alert-danger" v-if="error">{{ error }}</div>
    </div>
    <button v-on:click="login" class="btn btn-outline-danger mt-1">Se connecter</button>
</div>
</template>

<script>
import router from '../router';
import quizApiService from '../services/quizApiService';
import localStorageService from '../services/LocalStorageService';
export default {
  name: "LoginPage",
  data() {
    return {
      password : '',
      error : ''
    };
  },
  methods: {
    login() {
      quizApiService.login(this.password)
        .then((response) => {
          if (response.status === 200) {
            this.error ='';
            localStorageService.saveToken(response.data.token);
            router.push('/admin');
          }else if(response.status === 401){
            this.error = response.data
          }
        });
    }
  },
  async created() {
  }
};
</script>

<style scoped>
</style>