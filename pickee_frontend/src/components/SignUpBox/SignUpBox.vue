<template>
    <v-card class="auth-box" light>
        <h1 class="auth-box__header">Sign Up</h1>
        <div class="auth-box__errors" v-if="data.errors">
            <template v-for="(fieldErrors, fieldName) in data.errors">
                <template v-for="error in fieldErrors">
                    <p v-bind:key="fieldName + error">{{ fieldName }}: {{ error }}</p>
                </template>
            </template>
        </div>
        <form method="post" :action="actionUrl">
            <input type="hidden" name="csrfmiddlewaretoken" :value="token">
            <FormTextField type="text" label="Email" name="email" />
            <FormTextField type="password" label="Password" name="password1" />
            <FormTextField type="password" label="Password confirmation" name="password2" />
            <v-btn class="auth-box__submit" type="submit" color="primary">Sign Up</v-btn>
        </form>

        <a class="auth-box__signup-link" :href="loginUrl">Login</a>
    </v-card>
</template>

<script src="./SignUpBox.js" />
