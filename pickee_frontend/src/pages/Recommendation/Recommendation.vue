<template>
    <v-app>
        <div class="page-wrapper page-recommendation">
            <PageHeader logo />
            <v-content>
                <RecommendationBox />
            </v-content>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from "@/components/PageHeader/PageHeader.vue";
    import RecommendationBox from "@/components/RecommendationBox/RecommendationBox.vue";
    
    export default {
        name: "Recommendation",
        data: () => ({}),
        methods: {},
        components: {
            PageHeader,
            RecommendationBox
        }
    };
</script>
