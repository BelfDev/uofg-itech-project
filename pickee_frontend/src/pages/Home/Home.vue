<template>
    <v-app>
        <div class="page-home">
            <v-content>
                <div class="page-home-screen page-home-screen--1 page-home-screen--active">
                    <div class="page-home-content">
                        <PageHeader />
                        <Intro />
                    </div>
                </div>
                <div class="page-home-screen page-home-screen--2">
                    <div class="page-home-content">
                        <PageHeader />
                        <div>Form</div>
                    </div>
                </div>
                <div class="page-home-content-bg"></div>
                <div class="stripe stripe--light"></div>
                <div class="stripe stripe--lighter"></div>
                <div class="stripe stripe--dark"></div>
            </v-content>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from '@/components/PageHeader/PageHeader.vue';
    import Intro from '@/components/Intro/Intro.vue';

    export default {
        name: "Home",
        data: () => ({}),
        methods: {},
        components: {
            PageHeader,
            Intro
        }
    };
</script>
