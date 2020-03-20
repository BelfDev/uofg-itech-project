<template>
    <div class="recommendation-box">
        <RecommendationCarousel ref="recCarousel" :recommendation="recData" />
        <RecommendationDescr :recommendation="recData" :newRecEvent="getNewRecommendation" />
    </div>
</template>

<script src="./RecommendationBox.js" />
<style src="./RecommendationBox.css" />
