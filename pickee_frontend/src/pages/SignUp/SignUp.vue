<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader logo />
            <v-content class="page-content page-content--centered">
                <SignUpBox :actionUrl="urls.signup" :loginUrl="urls.login" :data="data"  />
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
        data: {},
        urls: {}
    }),
    methods: {},
    components: { PageHeader, SignUpBox },
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
