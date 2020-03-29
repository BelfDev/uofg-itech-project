import "swiper/dist/css/swiper.css";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import { mdiChevronLeft, mdiChevronRight, mdiThumbDown, mdiThumbUp, mdiBookmark } from '@mdi/js';

export default {
    name: "RecommendationCarousel",
    props: ['recommendation', 'isLoading', 'showPrevRec', 'showNextRec', 'activeSlideIndex'],
    components: {
        swiper,
        swiperSlide,
    },
    methods: {
        setNewRecommendation: function(recommendation, prevChoice) {
            this.swiperSlides[this.activeSlideIndex].user_choice = prevChoice;

            if (prevChoice === 'ACCEPTED')
                return false;

            if (recommendation) {
                this.swiperSlides.push({
                    recommendationID: recommendation.recommendation_id,
                    image_url: recommendation.image_url,
                    name: recommendation.name,
                    user_choice: null
                });

                setTimeout(() => {
                    this.$refs.mySwiper.swiper.slideTo(this.swiperSlides.length - 1)
                }, 100);
            }
        }
    },
    mounted: function() {
        this.swiperSlides.push({
            image_url: this.recommendation.image_url,
            name: this.recommendation.name,
            user_choice: null 
        })
    },
    data() {
        return {
            iconArrowLeft: mdiChevronLeft,
            iconArrowRight: mdiChevronRight,
            iconFavorites: mdiBookmark,
            iconThumbDown: mdiThumbDown,
            iconThumbUp: mdiThumbUp,
            swiperSlides: [],
            swiperOption: {
                effect: "coverflow",
                centeredSlides: true,
                initialSlide: 1,
                slidesPerView: "auto",
                spaceBetween: 0,
                grabCursor: false,
                simulateTouch: false,
                navigation: {
                    nextEl: '.recommendation-carousel__swiper-button-next',
                    prevEl: '.recommendation-carousel__swiper-button-prev',
                },
                coverflowEffect: {
                    rotate: 0,
                    stretch: 0,
                    depth: 20,
                    modifier: 20,
                    slideShadows: false
                }
            }
        };
    }
};
