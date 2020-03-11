<template>
    <v-card class="auth-box" light>
        <h1 class="auth-box__header">Login</h1>
        <FormTextField label="Username" />
        <FormTextField label="Password" />
        <v-btn class="auth-box__submit" color="primary">Login</v-btn>
        <a class="auth-box__signup-link" href="#">Create Account</a>
    </v-card>
</template>

<script src="./LoginBox.js" />
