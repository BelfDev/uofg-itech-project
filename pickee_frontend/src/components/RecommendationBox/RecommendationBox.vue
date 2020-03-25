<template>
    <div class="recommendation-box">
        <div class="mx-auto">
            <v-progress-circular
                :size="140"
                :width="7"
                color="primary"
                v-if="isInitialLoading"
                indeterminate
            ></v-progress-circular>
        </div>
        
        <template v-if="!isInitialLoading && recData.id">
            <RecommendationCarousel ref="recCarousel" :recommendation="recData" :isLoading="isLoading" />
            <RecommendationDescr 
                :recommendation="recData" 
                :providerList="providerList"
                :newRecEvent="getNewRecommendation" 
                :acceptEvent="getProviderList" 
                :isLoading="isLoading"
            />
        </template>
    </div>
</template>

<script src="./RecommendationBox.js" />
<style src="./RecommendationBox.css" />
