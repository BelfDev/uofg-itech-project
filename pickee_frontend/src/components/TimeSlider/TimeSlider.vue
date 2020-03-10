<template>
    <div class="time-slider">
        <span class="time-slider__label">{{ timePretty }}</span>
        <div class="time-slider__input">
            <v-slider
                v-model="minutes"
                step="30"
                min="30"
                max="240"
                ticks
            ></v-slider>
        </div>
    </div>
</template>

<script src="./TimeSlider.js"></script>
<style src="./TimeSlider.css"></style>
