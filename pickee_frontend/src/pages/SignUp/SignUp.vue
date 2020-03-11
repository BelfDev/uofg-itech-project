<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader logo />
            <v-content class="page-content page-content--centered">
                <SignUpBox />
            </v-content>
        </div>
    </v-app>
</template>

<script>
import PageHeader from "@/components/PageHeader/PageHeader.vue";
import SignUpBox from "@/components/SignUpBox/SignUpBox.vue";

export default {
    name: "SignUp",
    data: () => ({}),
    methods: {},
    components: { PageHeader, SignUpBox }
};
</script>
