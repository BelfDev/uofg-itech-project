<template>
    <div class="profile-header">
        <v-avatar class="profile-header__avatar" size="19.2rem">
            <img :src="user.picture" :alt="user.name" v-if="user.picture" />
            <v-icon size="10rem" color="white" v-else>{{ iconUser }}</v-icon>
        </v-avatar>
        <div class="profile-header__content">
            <h2 class="profile-header__name">{{ user.name}}</h2>
            <p class="profile-header__time-saved">200 minutes saved</p>
        </div>
    </div>
</template>
<script src="./ProfileHeader.js" />
<style src="./ProfileHeader.css" />
