<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader />
            <v-content>
                <Logo />
                <p>Login</p>
            </v-content>
        </div>
    </v-app>
</template>

<script>
import Logo from "@/components/Logo/Logo.vue";
import PageHeader from "@/components/PageHeader/PageHeader.vue";

export default {
    name: "Login",
    data: () => ({}),
    methods: {},
    components: { Logo, PageHeader }
};
</script>

<style>
#Login {
    margin: 20px;
}
</style>
