<template>
    <v-app>
        <div class="page-wrapper about-page">
            <PageHeader />
            <v-content class="page-content">
                       <h1>We are<br /> <span class="heading1-accent">Pickee.</span></h1>
            </v-content>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from "@/components/PageHeader/PageHeader.vue";

    export default {
        name: "About",
        data: () => ({}),
        methods: {},
        components: { PageHeader }
    };
</script>


