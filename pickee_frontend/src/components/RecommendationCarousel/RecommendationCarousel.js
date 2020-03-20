import "swiper/dist/css/swiper.css";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import { mdiChevronLeft, mdiChevronRight, mdiThumbDown, mdiThumbUp, mdiBookmark } from '@mdi/js';

export default {
    name: "RecommendationCarousel",
    props: ['recommendation'],
    components: {
        swiper,
        swiperSlide,
    },
    methods: {
        setNewRecommendation: function(data) {
            this.swiperSlides.push({
                image_url: data.recommendation.image_url,
                name: data.recommendation.name
            });

            setTimeout(() => {
                this.$refs.mySwiper.swiper.slideNext()
            }, 100);
        }
    },
    data() {
        return {
            iconArrowLeft: mdiChevronLeft,
            iconArrowRight: mdiChevronRight,
            iconFavorites: mdiBookmark,
            iconThumbDown: mdiThumbDown,
            iconThumbUp: mdiThumbUp,
            swiperSlides: [{
                image_url: this.recommendation.image_url,
                name: this.recommendation.name
            }],
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
