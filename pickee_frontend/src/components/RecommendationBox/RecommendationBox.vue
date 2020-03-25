<template>
    <div class="recommendation-box">
        <div class="mx-auto">
            <v-progress-circular
                :size="140"
                :width="7"
                color="primary"
                v-if="isLoading"
                indeterminate
            ></v-progress-circular>
        </div>
        
        <template v-if="!isLoading && recData.id">
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
