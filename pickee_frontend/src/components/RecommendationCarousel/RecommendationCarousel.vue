<template>
    <div class="recommendation-carousel">
        <swiper :options="swiperOption" ref="mySwiper" class="recommendation-carousel__swiper">
            <swiper-slide
                class="recommendation-carousel__swiper-slide"
                v-for="slide in swiperSlides"
                :key="slide.name"
            >
                <img :src="`https://image.tmdb.org/t/p/w500/${slide.image_url}`" :alt="slide.name" />
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