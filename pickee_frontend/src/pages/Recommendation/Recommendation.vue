<template>
    <v-app>
        <div class="page-wrapper page-recommendation">
            <PageHeader :user="data.user" logo />
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
        data: () => ({
            data: {},
        }),
        methods: {},
        components: {
            PageHeader,
            RecommendationBox
        },
        beforeMount() {
            const appElement = document.getElementsByTagName('app')[0];
            const data = appElement.getAttribute('data');
            if (data) {
                this.data = JSON.parse(data);
            }
        }
    };
</script>
