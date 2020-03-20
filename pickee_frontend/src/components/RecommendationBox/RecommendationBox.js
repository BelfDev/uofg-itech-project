import RecommendationCarousel from "@/components/RecommendationCarousel/RecommendationCarousel.vue";
import RecommendationDescr from "@/components/RecommendationDescr/RecommendationDescr.vue";

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
        getNewRecommendation: function(userChoice) {
            // SEND RECOMMENDATION USER CHOICE REQUEST HERE

            // RECEIVE NEW ONE
            const data = {
                "recommendation": {
                    "id": 122,
                    "name": "The Lord of the Rings: The Return of the King",
                    "image_url": "/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
                    "rating": "8.4",
                    "release_date": "2003-12-01",
                    "description": "Aragorn is revealed as the heir to the ancient kings as he, Gandalf and the other members of the broken fellowship struggle to save Gondor from Sauron's forces. Meanwhile, Frodo and Sam take the ring closer to the heart of Mordor, the dark lord's realm.",
                    "cast": [
                        {
                            "id": 109,
                            "name": "Elijah Wood",
                        },
                        {
                            "cast_id": 13,
                            "name": "Ian McKellen",
                        }
                    ]
                }
            };

            this.recData = data.recommendation;

            this.$refs.recCarousel.setNewRecommendation(data, userChoice);
        }
    },
    components: {
        RecommendationCarousel,
        RecommendationDescr
    }
}