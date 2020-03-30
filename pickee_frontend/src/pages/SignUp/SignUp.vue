<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader logo />
            <v-content class="page-content page-content--centered">
                <SignUpBox :actionUrl="actionUrl" :loginUrl="loginUrl" :data="data"  />
            </v-content>
        </div>
    </v-app>
</template>

<script>
import PageHeader from "@/components/PageHeader/PageHeader.vue";
import SignUpBox from "@/components/SignUpBox/SignUpBox.vue";

export default {
    name: "SignUp",
    data: () => ({
        actionUrl: '',
        loginUrl: '',
        data: {}
    }),
    methods: {},
    components: { PageHeader, SignUpBox },
    beforeMount() {
        const appElement = document.getElementsByTagName('app')[0];
        this.actionUrl = appElement.getAttribute('actionUrl');
        this.loginUrl = appElement.getAttribute('loginUrl');
        const data = appElement.getAttribute('data');
        if (data) {
            this.data = JSON.parse(data);
        }
    }
};
</script>
