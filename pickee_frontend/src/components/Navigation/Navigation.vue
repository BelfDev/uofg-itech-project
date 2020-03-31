<template>
    <nav class="header-nav">
        <a class="link" :href="urls.about" v-if="!isAboutPage">About Us</a>
        <a class="link" :href="urls.home" v-if="isAboutPage">Home</a>
    </nav>
</template>

<script src="./Navigation.js" />
