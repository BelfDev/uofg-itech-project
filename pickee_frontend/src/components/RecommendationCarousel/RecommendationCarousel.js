import "swiper/dist/css/swiper.css";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import { mdiChevronLeft, mdiChevronRight, mdiThumbDown, mdiBookmark } from '@mdi/js';

export default {
    name: "RecommendationCarousel",
    props: ['recommendation'],
    components: {
        swiper,
        swiperSlide,
    },
    methods: {
        setNewRecommendation: function(recommendation, prevChoice) {
            this.swiperSlides.push({
                recommendationID: recommendation.recommendation_id,
                image_url: recommendation.image_url,
                name: recommendation.name,
                user_choice: null
            });

            if (prevChoice) {
                this.swiperSlides[this.lastSlideIndex].user_choice = prevChoice;
            }
            this.lastSlideIndex++;

            setTimeout(() => {
                if (this.$refs.mySwiper) {
                    this.$refs.mySwiper.swiper.slideNext()
                }
            }, 100);
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
            lastSlideIndex: 0,
            iconArrowLeft: mdiChevronLeft,
            iconArrowRight: mdiChevronRight,
            iconFavorites: mdiBookmark,
            iconThumbDown: mdiThumbDown,
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
