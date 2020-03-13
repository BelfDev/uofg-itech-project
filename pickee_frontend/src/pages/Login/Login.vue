<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader />
            <v-content class="page-content">
                <LoginBox :formUrl="formUrl" />
            </v-content>
        </div>
    </v-app>
</template>

<script>
import PageHeader from "@/components/PageHeader/PageHeader.vue";
import LoginBox from "@/components/LoginBox/LoginBox.vue";

export default {
    name: "Login",
    data: function() {
        return {
            formUrl: window.formOptions.url
        };
    },
    methods: {},
    components: { PageHeader, LoginBox }
};
</script>