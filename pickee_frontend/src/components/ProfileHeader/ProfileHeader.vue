<template>
    <div class="profile-header">
        <div class="profile-header__top">
            <v-btn text rounded class="profile-header__avatar-btn">
                <v-avatar class="profile-header__avatar" size="19.2rem">
                    <v-file-input 
                        v-model="avatarFile"
                        accept="image/*"
                        solo
                        :prepend-icon="''"
                        @change="uploadAvatar"
                    ></v-file-input>
                    <img :src="user.picture" :alt="user.name" v-if="user.picture" />
                    <v-icon color="white" v-else>{{ iconUser }}</v-icon>
                </v-avatar>
            </v-btn>
            <div class="profile-header__content">
                <h2 class="profile-header__name">{{ user.name}}</h2>
            </div>
        </div>
        <div class="profile-header__error" v-if="errorAvatarUpload.length > 0">{{errorAvatarUpload}}</div>
    </div>
</template>
<script src="./ProfileHeader.js" />
<style src="./ProfileHeader.css" />
