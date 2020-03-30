<template>
    <nav class="header-nav">
        <a class="link" href="/about/" v-if="!isAboutPage">About Us</a>
        <a class="link" href="/" v-if="isAboutPage">Home</a>
    </nav>
</template>

<script src="./Navigation.js" />
