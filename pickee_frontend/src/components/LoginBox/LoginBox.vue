<template>
    <v-card class="auth-box" light>
        <h1 class="auth-box__header">Login</h1>
        <div class="auth-box__errors" v-if="data.error">{{ data.error }}</div>
        <form id="login_form" method="post" :action="actionUrl">
            <input type="hidden" name="csrfmiddlewaretoken" :value="token">
            <FormTextField type="text" label="Email" name="email" />
            <FormTextField type="password" label="Password" name="password" />
            <v-btn class="auth-box__submit" type="submit" color="primary">Login</v-btn>
        </form>
        <a class="auth-box__signup-link" :href="signupUrl">Create Account</a>
    </v-card>
</template>

<script src="./LoginBox.js" />
