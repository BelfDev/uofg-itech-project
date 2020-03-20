<template>
    <div class="recommendation-box">
        <RecommendationCarousel ref="recCarousel" :recommendation="recommendation" />
        <RecommendationDescr :recommendation="recommendation" :rejectEvent="getNewRecommendation" />
    </div>
</template>

<script src="./RecommendationBox.js" />
<style src="./RecommendationBox.css" />
