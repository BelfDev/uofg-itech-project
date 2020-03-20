import RecommendationCarousel from "@/components/RecommendationCarousel/RecommendationCarousel.vue";
import RecommendationDescr from "@/components/RecommendationDescr/RecommendationDescr.vue";

export default {
    name: "RecommendationBox",
    props: ['recommendation', 'setNewRecommendation'],
    data: () => ({
        data: {}
    }),
    methods: {
        getNewRecommendation: function() {
            const data = {
                "recommendation": {
                    "id": 122,
                    "name": "The Lord of the Rings: The Return of the King",
                    "image_url": "/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
                    "rating": "8.4",
                    "release_date": "2003-12-01",
                    "description": "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.",
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

            this.$refs.recCarousel.setNewRecommendation(data);
        }
    },
    components: {
        RecommendationCarousel,
        RecommendationDescr
    }
}