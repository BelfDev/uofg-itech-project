<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader />
            <v-content class="page-content">
                <LoginBox :actionUrl="actionUrl" :signupUrl="signupUrl" :data="data" />
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
            actionUrl: '',
            signupUrl: '',
            data: {}
        };
    },
    methods: {},
    components: { PageHeader, LoginBox },
    beforeMount() {
        const appElement = document.getElementsByTagName('app')[0];
        this.actionUrl = appElement.getAttribute('actionUrl');
        this.signupUrl = appElement.getAttribute('signupUrl');
        const data = appElement.getAttribute('data');
        if (data) {
            this.data = JSON.parse(data);
        }
    }
};
</script>