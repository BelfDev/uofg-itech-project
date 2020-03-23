<template>
    <div class="recommendation-carousel">
        <swiper :options="swiperOption" ref="mySwiper" class="recommendation-carousel__swiper">
            <swiper-slide
                class="recommendation-carousel__swiper-slide"
                v-for="slide in swiperSlides"
                :key="slide.name"
            >
                <div class="action-button" v-if="slide.user_choice === 'REJECTED'">
                    <v-icon color="red" size="4.5rem">{{ iconThumbDown }}</v-icon>
                </div>
                <div class="action-button" v-else-if="slide.user_choice === 'BOOKMARKED'">
                    <v-icon color="primary" size="4.5rem">{{ iconFavorites }}</v-icon>
                </div>
                <template v-if="slide.image_url">
                    <img :src="slide.image_url" :alt="slide.name" />
                </template>
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