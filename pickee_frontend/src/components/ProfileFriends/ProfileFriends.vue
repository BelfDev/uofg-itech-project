<template>
    <div class="content-card-box">
        <h3 class="content-card-box__header">Friends</h3>
        <v-card dark>
            <v-card-text>
                <ItemList :items="items" :button-action="removeFriend" />
            </v-card-text>
        </v-card> 
    </div>
</template>

<script src="./ProfileFriends.js" />
<style src="./ProfileFriends.css" />
