<template>
    <v-app>
        <v-content>
            <Logo />
            <p>Login</p>
        </v-content>
    </v-app>
</template>

<script>
import Logo from "@/components/Logo/Logo.vue";
export default {
    name: "Login",
    data: () => ({}),
    methods: {},
    components: { Logo }
};
</script>

<style>
#Login {
    margin: 20px;
}
</style>
