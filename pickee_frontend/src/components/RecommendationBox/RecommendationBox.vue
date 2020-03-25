<template>
    <div class="recommendation-box" v-if="recData.id">
        <RecommendationCarousel ref="recCarousel" :recommendation="recData" />
        <RecommendationDescr 
            :recommendation="recData" 
            :providerList="providerList"
            :newRecEvent="getNewRecommendation" 
            :acceptEvent="getProviderList" 
        />
    </div>
</template>

<script src="./RecommendationBox.js" />
<style src="./RecommendationBox.css" />
