<template>
    <v-app>
        <div class="page-home">
            <v-content>
                <div class="page-home-content">
                    <PageHeader />
                </div>
                <div class="page-home-content-bg"></div>
                <div class="stripe stripe--dark"></div>
                <div class="stripe stripe--light"></div>
                <div class="stripe stripe--lighter"></div>
            </v-content>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from '@/components/PageHeader/PageHeader.vue';

    export default {
        name: "Home",
        data: () => ({}),
        methods: {},
        components: {
            PageHeader
        }
    };
</script>
