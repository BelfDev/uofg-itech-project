<template>
    <header class="page-header">
        <Logo v-if="logo"/>
        <Navigation />
        <HeaderAuth :user="user" />
    </header>
</template>

<script src="./PageHeader.js" />
<style src="./PageHeader.css" />