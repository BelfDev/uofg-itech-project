<template>
    <v-app>
        <div class="page-wrapper page-recommendation">
            <PageHeader :user="user" :urls="urls" logo />
            <v-content>
                <RecommendationBox :user="user" :preferences="preferences" :urls="urls" />
            </v-content>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from "@/components/PageHeader/PageHeader.vue";
    import RecommendationBox from "@/components/RecommendationBox/RecommendationBox.vue";
    
    export default {
        name: "Recommendation",
        data: () => ({
            user: {},
            recommendation: {},
            urls: {}
        }),
        methods: {},
        components: {
            PageHeader,
            RecommendationBox
        },
        beforeMount() {
            const appElement = document.getElementsByTagName('app')[0];
            const user = appElement.getAttribute('user');
            const urls = appElement.getAttribute('urls');
            const preferences = appElement.getAttribute('preferences');
            if (user && preferences) {
                this.user = JSON.parse(user);
                this.preferences = JSON.parse(preferences);
            }
            if (urls) {
                this.urls = JSON.parse(urls);
            }
        }
    };
</script>
