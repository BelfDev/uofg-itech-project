<template>
    <div class="time-slider">
        <span class="time-slider__label">{{ timePretty }}</span>
        <div class="time-slider__input">
            <v-slider
                v-model="minutes"
                :name="name"
                color="white"
                thumb-color="primary"
                step="30"
                min="30"
                max="240"
                height="16"
                ticks
            ></v-slider>
        </div>
    </div>
</template>

<script src="./TimeSlider.js" />
<style src="./TimeSlider.css" />
