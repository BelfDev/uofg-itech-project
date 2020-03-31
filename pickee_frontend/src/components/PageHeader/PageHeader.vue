<template>
    <header class="page-header">
        <Logo :urls="urls" v-if="logo"/>
        <Navigation :urls="urls" :isAboutPage="isAboutPage" />
        <HeaderAuth :urls="urls" v-if="user" :user="user" />
    </header>
</template>

<script src="./PageHeader.js" />
<style src="./PageHeader.css" />