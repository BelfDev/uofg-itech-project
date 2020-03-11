<template>
    <v-app>
        <div class="page-wrapper">
            <Navigation />
            <v-content>
                <Logo />
                <p>Login</p>
            </v-content>
        </div>
    </v-app>
</template>

<script>
import Logo from "@/components/Logo/Logo.vue";
import Navigation from "@/components/Navigation/Navigation.vue";

export default {
    name: "Login",
    data: () => ({}),
    methods: {},
    components: { Logo, Navigation }
};
</script>

<style>
#Login {
    margin: 20px;
}
</style>
