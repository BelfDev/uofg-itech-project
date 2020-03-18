<template>
    <div class="recommendation-carousel">
        <swiper :options="swiperOption" ref="mySwiper" class="recommendation-carousel__swiper">
            <!-- slides -->
            <swiper-slide class="recommendation-carousel__swiper-slide">
                <img src="https://image.tmdb.org/t/p/w500/xBHvZcjRiWyobQ9kxBhO6B2dtRI.jpg" alt="Ad Astra" />
            </swiper-slide>
            <swiper-slide class="recommendation-carousel__swiper-slide">
                <img src="https://image.tmdb.org/t/p/w500/eFCzU9Jqp2Ea17ysDkG8PB0NLiR.jpg" alt="A Rainy Day in New York" />
            </swiper-slide>
            <swiper-slide class="recommendation-carousel__swiper-slide">
                <img src="https://image.tmdb.org/t/p/w500/aQvJ5WPzZgYVDrxLX4R6cLJCEaQ.jpg" alt="Sonic the Hedgehog" />
            </swiper-slide>
            <swiper-slide class="recommendation-carousel__swiper-slide">
                <img src="https://image.tmdb.org/t/p/w500/db32LaOibwEliAmSL2jjDF6oDdj.jpg" alt="Star Wars: The Rise of Skywalker" />
            </swiper-slide>
            <swiper-slide class="recommendation-carousel__swiper-slide">
                <img src="https://image.tmdb.org/t/p/w500/iZf0KyrE25z1sage4SYFLCCrMi9.jpg" alt="1917" />
            </swiper-slide>
        </swiper>
        <button class="recommendation-carousel__swiper-button-prev" slot="button-prev">
            <v-icon size="6.5rem">{{ iconArrowLeft }}</v-icon>
        </button>
        <button class="recommendation-carousel__swiper-button-next" slot="button-next">
            <v-icon size="6.5rem">{{ iconArrowRight }}</v-icon>
        </button>
    </div>
</template>

<script src="./RecommendationCarousel.js" />
<style src="./RecommendationCarousel.css" />