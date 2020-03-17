<template>
    <v-app>
        <div class="page-home">
            <v-content>
                <div class="page-home-screen page-home-screen--1">
                    <div class="page-home-content">
                        <PageHeader />
                        <Intro />
                    </div>
                    <div class="page-home-content-bg"></div>
                    <div class="stripe stripe--light"></div>
                    <div class="stripe stripe--lighter"></div>
                    <div class="stripe stripe--dark"></div>
                </div>
                <div class="page-home-screen page-home-screen--2 page-home-screen--active">
                    <div class="page-home-content">
                        <PageHeader />
                        <CasualPreferencesSelection />
                    </div>
                    <div class="stripe stripe--alt stripe--light"></div>
                    <div class="stripe stripe--alt stripe--lighter"></div>
                </div>
            </v-content>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from '@/components/PageHeader/PageHeader.vue';
    import Intro from '@/components/Intro/Intro.vue';
    import CasualPreferencesSelection from '@/components/CasualPreferencesSelection/CasualPreferencesSelection.vue';

    export default {
        name: "Home",
        data: () => ({}),
        methods: {},
        components: {
            PageHeader,
            Intro,
            CasualPreferencesSelection
        }
    };
</script>
