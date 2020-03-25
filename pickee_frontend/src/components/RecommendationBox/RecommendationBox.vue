<template>
    <div class="recommendation-box" v-if="recData.id">
        <div class="text-center flex">
            <v-progress-circular
                :size="70"
                :width="7"
                color="primary"
                v-if="isLoading"
                indeterminate
            ></v-progress-circular>
        </div>
        
        <template v-if="!isLoading">
            <RecommendationCarousel ref="recCarousel" :recommendation="recData" />
            <RecommendationDescr 
                :recommendation="recData" 
                :providerList="providerList"
                :newRecEvent="getNewRecommendation" 
                :acceptEvent="getProviderList" 
            />
        </template>
    </div>
</template>

<script src="./RecommendationBox.js" />
<style src="./RecommendationBox.css" />
