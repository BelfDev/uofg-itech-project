import "swiper/dist/css/swiper.css";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import { mdiChevronLeft, mdiChevronRight, mdiThumbDown, mdiThumbUp, mdiBookmark } from '@mdi/js';

export default {
    name: "RecommendationCarousel",
    components: {
        swiper,
        swiperSlide,
    },
    data() {
        return {
            iconArrowLeft: mdiChevronLeft,
            iconArrowRight: mdiChevronRight,
            iconFavorites: mdiBookmark,
            iconThumbDown: mdiThumbDown,
            iconThumbUp: mdiThumbUp,
            swiperOption: {
                effect: "coverflow",
                centeredSlides: true,
                initialSlide: 4,
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
