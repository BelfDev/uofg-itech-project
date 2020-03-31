<template>
    <div class="recommendation-carousel">
        <swiper 
            :options="swiperOption" 
            ref="mySwiper" 
            class="recommendation-carousel__swiper"
        >
            <swiper-slide
                class="recommendation-carousel__swiper-slide"
                v-for="slide in swiperSlides"
                :key="slide.recommendationID"
            >
                <div class="action-button" v-if="slide.user_choice === 'REJECTED'">
                    <v-icon color="red">{{ iconThumbDown }}</v-icon>
                </div>
                <div class="action-button" v-if="slide.user_choice === 'BOOKMARKED'">
                    <v-icon color="primary">{{ iconFavorites }}</v-icon>
                </div>
                <div class="action-button" v-if="slide.user_choice === 'ACCEPTED'">
                    <v-icon color="green">{{ iconThumbUp }}</v-icon>
                </div>

                <img :src="slide.image_url" :alt="slide.name" v-if="slide.image_url" />
                <div class="recommendation-carousel__empty-poster" v-else><span>Poster not yet available</span></div>
            </swiper-slide>
        </swiper>
        <button class="recommendation-carousel__swiper-button-prev" slot="button-prev" @click="showPrevRec">
            <v-icon>{{ iconArrowLeft }}</v-icon>
        </button>
        <button class="recommendation-carousel__swiper-button-next" slot="button-next" @click="showNextRec">
            <v-icon>{{ iconArrowRight }}</v-icon>
        </button>
    </div>
</template>

<script src="./RecommendationCarousel.js" />
<style src="./RecommendationCarousel.css" />