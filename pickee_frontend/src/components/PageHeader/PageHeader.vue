<template>
    <header class="page-header">
        <Logo v-if="logo"/>
        <Navigation isAboutPage />
        <HeaderAuth v-if="user" :user="user" />
    </header>
</template>

<script src="./PageHeader.js" />
<style src="./PageHeader.css" />