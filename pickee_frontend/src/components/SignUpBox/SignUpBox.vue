<template>
    <v-card class="auth-box" light>
        <h1 class="auth-box__header">Sign Up</h1>
        <FormTextField label="Username" />
        <FormTextField label="Password" />
        <v-btn class="auth-box__submit" color="primary">Create Account</v-btn>
        <a class="auth-box__signup-link" href="#">Login</a>
    </v-card>
</template>

<script src="./SignUpBox.js" />
