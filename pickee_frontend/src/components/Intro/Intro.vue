<template>
    <div class="intro">
        <h1 class="intro__heading">Feeling<br />
            <span class="heading1-accent">Pickee?</span>
        </h1>
        <div class="label-accented">Save the thrill for the picture</div>
        <div class="intro__button">
            <v-btn rounded x-large color="primary" @click="changeScreenMethod">
                Pick a movie for me
                <v-icon class="ml-5">{{ iconArrowRight }}</v-icon>
            </v-btn>
        </div>
    </div>
</template>

<script src="./Intro.js" />
<style src="./Intro.css" />