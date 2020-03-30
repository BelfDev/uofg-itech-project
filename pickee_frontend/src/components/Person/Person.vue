<template>
    <div class="person">
        <v-avatar class="header-auth" size="128">
            <img :src="avatar" :alt="name" />
        </v-avatar>
        <div class="person__info"> 
            <h3 class="person__name">{{ name }}</h3>
            <p class="person__role">{{ role }}</p>
        </div>
    </div>
</template>

<script src="./Person.js" />
<style src="./Person.css" />
