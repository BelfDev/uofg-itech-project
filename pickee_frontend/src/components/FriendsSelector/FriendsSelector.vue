<template>
    <div class="friends-selector">
        <v-avatar 
            class="friends-selector__selected-item" 
            size="16rem" 
            v-for="friend in selectedFriends" 
            v-bind:key="friend.id"
        >
            <img :src="friend.avatar" :alt="friend.name" />
        </v-avatar>
        
        <v-avatar class="friends-selector__selector" size="16rem">
            <v-icon class="friends-selector__selector-icon" size="8rem">{{ iconPlus }}</v-icon>
        </v-avatar>
    </div>
</template>

<script src="./FriendsSelector.js" />
<style src="./FriendsSelector.css" />