<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader logo />
            <v-content class="page-content">
                <LoginBox :actionUrl="urls.login" :signupUrl="urls.signup" :data="data" />
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
            data: {},
            urls: {}
        };
    },
    methods: {},
    components: { PageHeader, LoginBox },
    beforeMount() {
        const appElement = document.getElementsByTagName('app')[0];
        let urls = appElement.getAttribute('urls');
        const data = appElement.getAttribute('data');
        if (data) {
            this.data = JSON.parse(data);
        }
        if (urls) {
            this.urls = JSON.parse(urls);
            console.log(this.urls)
        }
    }
};
</script>