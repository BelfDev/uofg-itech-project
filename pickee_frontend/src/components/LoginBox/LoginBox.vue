<template>
    <v-card class="login-box" light>
        <h1 class="login-box__header">LOGIN</h1>
        <FormTextField label="Username" />
        <FormTextField label="Password" />
        <v-btn class="login-box__submit" color="primary">Login</v-btn>
        <a class="login-box__signup-link" href="#">Create Account</a>
    </v-card>
</template>

<script src="./LoginBox.js" />
<style src="./LoginBox.css" />