<template>
    <v-app>
        <div class="page-wrapper page-recommendation">
            <PageHeader :user="user" logo />
            <v-content>
                <RecommendationBox :user="user" :preferences="preferences" />
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
        }),
        methods: {},
        components: {
            PageHeader,
            RecommendationBox
        },
        beforeMount() {
            const appElement = document.getElementsByTagName('app')[0];
            const user = appElement.getAttribute('user');
            const preferences = appElement.getAttribute('preferences');
            if (user && preferences) {
                this.user = JSON.parse(user);
                this.preferences = JSON.parse(preferences);
            }
        }
    };
</script>
