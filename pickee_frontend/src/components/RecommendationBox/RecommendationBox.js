import RecommendationCarousel from "@/components/RecommendationCarousel/RecommendationCarousel.vue";
import RecommendationDescr from "@/components/RecommendationDescr/RecommendationDescr.vue";
import http from "@/services/http";

export default {
    name: "RecommendationBox",
    props: ['recommendation', 'setNewRecommendation'],
    data: () => ({
        data: {},
        recData: {}
    }),
    created: function() {
        this.recData = this.recommendation
    },
    methods: {
        getNewRecommendation: async function(userChoice) {
            // SEND RECOMMENDATION USER CHOICE REQUEST HERE

            // RECEIVE NEW ONE
            const response = await http.getRecommendation(userChoice);
            
            this.recData = response;

            this.$refs.recCarousel.setNewRecommendation(response, userChoice);
        }
    },
    components: {
        RecommendationCarousel,
        RecommendationDescr
    }
}