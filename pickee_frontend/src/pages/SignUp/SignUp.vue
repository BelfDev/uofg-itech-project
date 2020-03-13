<template>
    <v-app>
        <div class="page-wrapper">
            <PageHeader />
            <v-content class="page-content">
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
