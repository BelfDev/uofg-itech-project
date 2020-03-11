<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader />
            <v-content>
                <p>Login</p>
            </v-content>
        </div>
    </v-app>
</template>

<script>
import PageHeader from "@/components/PageHeader/PageHeader.vue";

export default {
    name: "Login",
    data: () => ({}),
    methods: {},
    components: { PageHeader }
};
</script>

<style>
#Login {
    margin: 20px;
}
</style>
