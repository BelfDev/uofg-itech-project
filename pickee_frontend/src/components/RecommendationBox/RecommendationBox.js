import RecommendationCarousel from "@/components/RecommendationCarousel/RecommendationCarousel.vue";
import RecommendationDescr from "@/components/RecommendationDescr/RecommendationDescr.vue";
import { mdiClose } from '@mdi/js';
import api from "@/services/api";

export default {
    name: "RecommendationBox",
    props: ['preferences', 'user', 'setNewRecommendation', 'urls'],
    data: function() {
        return {
            data: {},
            recData: {}, // recommendation data
            token: this.$cookies.get("csrftoken"),
            sessionID: null,
            offset: 1, // results offset to pass to the server
            providerList: [],
            isInitialLoading: true,
            isLoading: false,
            noResultsDialog: false,
            recommendationList: [],
            activeRecIndex: 0,
            lastRecIndex: 0,
            iconClose: mdiClose
        }
    },
    created: async function() {
        // It the user is not a guest (anonymous)
        // Create a session
        if (this.user.id) {
            this.preferences.user_ids = [
                    this.user.id+"", 
                    ...this.preferences.user_ids.split(',')
                        .filter(id => id != '')]
            const session = await api.createSession(this.preferences.user_ids);
            this.sessionID = session.id;
        }

        // Get recommendation request
        const recommendation = await api.getRecommendation(this.preferences, this.sessionID, 0);
        this.recommendationList.push(recommendation);

        // If the response is empty - show the corresponding dialog
        // - else pass the data
        if (recommendation.results && recommendation.total_results === 0) {
            this.noResultsDialog = true;
            this.recData = null;
        } else {
            this.recData = this.recommendationList[this.lastRecIndex];
            this.isInitialLoading = false;
        }
    },
    methods: {
        navigateBackToHome: function() {
            window.location.replace(`${this.urls.home}?step=2`);
        },
        getNewRecommendation: async function(userChoice) {
            this.isLoading = true;
            this.updateRecommendationStatus(userChoice);

            const recommendation = await api.getRecommendation(this.preferences, this.sessionID, this.offset);
            this.offset++;

            // If the response is empty - show the corresponding dialog
            // - else pass the data
            if (!recommendation || recommendation == {} || Object.keys(recommendation).length === 0) {
                this.noResultsDialog = true;

                // Trigger carousel update
                this.$refs.recCarousel.setNewRecommendation(null, userChoice);
            } else {
                this.recommendationList.push(recommendation);
                this.recData = this.recommendationList[++this.lastRecIndex];
                this.activeRecIndex = this.lastRecIndex;

                // Trigger carousel update
                this.$refs.recCarousel.setNewRecommendation(this.recData, userChoice);
            }

            this.isLoading = false;
        },
        showPrevRec: async function() {
            this.recData = this.recommendationList[--this.activeRecIndex];
        },
        showNextRec: async function() {
            this.recData = this.recommendationList[++this.activeRecIndex];
        },
        getProviderList: async function(userChoice) {
            this.isLoading = true;
            this.updateRecommendationStatus(userChoice);

            const response = await api.getProviderList(this.recData.name);
            
            // If response is not empty - prepare the list
            if (response && response != {} && Object.keys(response).length !== 0) {
                this.providerList = response.results.map(item => ({
                    logo: item.logo,
                    text: item.name,
                    link: item.url
                }));
            }

            // Trigger carousel update
            this.$refs.recCarousel.setNewRecommendation(this.recData, userChoice);
            this.isLoading = false;
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