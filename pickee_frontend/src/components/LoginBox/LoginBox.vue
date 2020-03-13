<template>
    <v-card class="auth-box" light>
        <h1 class="auth-box__header">Login</h1>
        <template v-if="data.error">{{ data.error }}</template>
        <form id="login_form" method="post" :action="actionUrl">
            <input type="hidden" name="csrfmiddlewaretoken" :value="token">
            <FormTextField label="Username" name="username" />
            <FormTextField label="Password" name="password" />
            <v-btn class="auth-box__submit" type="submit" color="primary">Login</v-btn>
        </form>
        <a class="auth-box__signup-link" href="#">Create Account</a>
    </v-card>
</template>

<script src="./LoginBox.js" />
