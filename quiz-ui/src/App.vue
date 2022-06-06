<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<div class="app-wrapper">
<img class="bg-image" src="@/assets/bg-4.jpg" alt="BG">
  <header>
    <div class="wrapper">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark px-2">
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

.bg-image{
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: fixed;
}

</style>
