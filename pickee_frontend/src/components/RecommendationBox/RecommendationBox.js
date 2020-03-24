import RecommendationCarousel from "@/components/RecommendationCarousel/RecommendationCarousel.vue";
import RecommendationDescr from "@/components/RecommendationDescr/RecommendationDescr.vue";
import api from "@/services/api";

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
        if (this.user.id) {
            this.preferences.user_ids = [
                    this.user.id+"", 
                    ...this.preferences.user_ids.split(',')
                        .filter(id => id != '')]
            const session = await api.createSession(this.preferences.user_ids);
            this.sessionID = session.id;
        }

        console.log(this.preferences);


        const recommendation = await api.getRecommendation(this.preferences, this.sessionID, 0);
        this.recData = recommendation;
    },
    methods: {
        getNewRecommendation: async function(userChoice) {
            this.updateRecommendationStatus(userChoice);

            const response = await api.getRecommendation(this.preferences, this.sessionID, this.offset);
            this.offset++;
            
            this.recData = response;
            this.$refs.recCarousel.setNewRecommendation(response, userChoice);
        },
        getProviderList: async function(userChoice) {
            this.updateRecommendationStatus(userChoice);
            const response = await api.getProviderList(this.recData.name);
            this.providerList = response.results.map(item => ({
                logo: item.logo,
                text: item.name,
                link: item.url
            }));
        },
        updateRecommendationStatus: async function(userChoice) {
            await api.setRecommendationUserChoice(this.recData.recommendation_id, this.sessionID, this.recData.id, userChoice);
        }
    },
    components: {
        RecommendationCarousel,
        RecommendationDescr
    }
}