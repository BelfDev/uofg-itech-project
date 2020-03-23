import RecommendationCarousel from "@/components/RecommendationCarousel/RecommendationCarousel.vue";
import RecommendationDescr from "@/components/RecommendationDescr/RecommendationDescr.vue";
import http from "@/services/http";

export default {
    name: "RecommendationBox",
    props: ['preferences', 'user', 'setNewRecommendation'],
    data: function() {
        return {
            data: {},
            recData: {},
            token: this.$cookies.get("csrftoken"),
            sessionID: null,
            offset: 1,
            providerList: []
        }
    },
    created: async function() {
        const preferences = this.preferences;
        if (preferences.user_ids) {
            preferences.user_ids = [this.user.id+"", ...preferences.user_ids.split(',')];
        }

        if (this.user.id) {
            const session = await http.createSession(preferences.user_ids, this.token);
            this.sessionID = session.id;
        }


        const recommendation = await http.getRecommendation(this.token, this.preferences, this.sessionID, 0);
        this.recData = recommendation;
    },
    methods: {
        getNewRecommendation: async function(userChoice) {
            this.updateRecommendationStatus(userChoice);

            const response = await http.getRecommendation(this.token, this.preferences, this.sessionID, this.offset);
            this.offset++;
            
            this.recData = response;
            this.$refs.recCarousel.setNewRecommendation(response, userChoice);
        },
        getProviderList: async function(userChoice) {
            this.updateRecommendationStatus(userChoice);
            const response = await http.getProviderList(this.recData.name);
            this.providerList = response.results.map(item => ({
                logo: item.logo,
                text: item.name,
                link: item.url
            }));
        },
        updateRecommendationStatus: async function(userChoice) {
            await http.setRecommendationUserChoice(this.token, this.recData.recommendation_id, this.sessionID, this.recData.id, userChoice);
        }
    },
    components: {
        RecommendationCarousel,
        RecommendationDescr
    }
}