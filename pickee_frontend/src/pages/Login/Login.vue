<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader />
            <v-content class="page-content">
                <LoginBox />
            </v-content>
        </div>
    </v-app>
</template>

<script>
import PageHeader from "@/components/PageHeader/PageHeader.vue";
import LoginBox from "@/components/LoginBox/LoginBox.vue";

export default {
    name: "Login",
    data: () => ({}),
    methods: {},
    components: { PageHeader, LoginBox }
};
</script>

<style>
#Login {
    margin: 20px;
}
</style>
