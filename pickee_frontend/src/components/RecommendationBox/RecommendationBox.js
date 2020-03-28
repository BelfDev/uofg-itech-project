import RecommendationCarousel from "@/components/RecommendationCarousel/RecommendationCarousel.vue";
import RecommendationDescr from "@/components/RecommendationDescr/RecommendationDescr.vue";
import { mdiClose } from '@mdi/js';
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
            providerList: [],
            isInitialLoading: true,
            isLoading: false,
            noResultsDialog: false,
            iconClose: mdiClose
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

        const recommendation = await api.getRecommendation(this.preferences, this.sessionID, 0);

        if (recommendation.results && recommendation.total_results === 0) {
            this.noResultsDialog = true;
            this.recData = null;
        } else {
            this.recData = recommendation;
            this.isInitialLoading = false;
        }
    },
    methods: {
        navigateBackToHome: function() {
            window.location.replace('/?step=2');
        },
        getNewRecommendation: async function(userChoice) {
            this.isLoading = true;
            this.updateRecommendationStatus(userChoice);

            const response = await api.getRecommendation(this.preferences, this.sessionID, this.offset);
            this.offset++;
            
            let recommendation = response;
            if (!response || response == {} || Object.keys(response).length === 0) {
                this.noResultsDialog = true;
                recommendation = null;
            } else {
                this.recData = response;
                this.isLoading = false;
            }

            this.$refs.recCarousel.setNewRecommendation(recommendation, userChoice);
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