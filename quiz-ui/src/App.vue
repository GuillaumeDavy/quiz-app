<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<div class="app-wrapper">

  <header>
    <div class="wrapper">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <span class="navbar-brand">Quiz-App</span>
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
        </div>
      </nav>
    </div>
  </header>
      </div>

  <RouterView />
</template>

<style>
@import '@/assets/base.css';

.app-wrapper{
  width: 100vw;
  height: 100vh;
  background-image: url('@/assets/bg-4.jpg');
    -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  }

</style>
