<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<div class="app-wrapper">
<img class="bg-image" src="@/assets/bg-4.jpg" alt="BG">
  <header>
    <div class="wrapper">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark px-2">
        <span class="navbar-brand navbar-title">Quiz-App</span>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <RouterLink to="/" class="nav-link">Accueil</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/admin" class="nav-link">Administration</RouterLink>
            </li>
          </ul>
          <div class="float-right contributors">
             Made by <a href="https://github.com/GuillaumeDavy" target="_blank">@GuillaumeDavy</a>
     / <a href="https://github.com/Vitrox77" target="_blank">@AlexandreJoudioux</a>
      / <a href="https://github.com/MatthiasJouen" target="_blank">@MatthiasJouen</a>
          </div>

        </div>
      </nav>
    </div>
  </header>
      </div>

  <RouterView />
  <footer class="bg-dark">
   
  </footer>
</template>

<style>
@import '@/assets/base.css';

.bg-image{
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: fixed;
}

.contributors {
  text-align:center;
  color: white;
  margin-left: auto;
}
.contributors a {
  color: #FE4B74;
  font-weight: 500;
  text-decoration: none;
}

.navbar-title {
	text-transform: uppercase;
	background: linear-gradient(to right, #0077ff 0%, #e40cc7 100%);
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
  font-size: 30px;
}

</style>
