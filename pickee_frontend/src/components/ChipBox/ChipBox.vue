<template>
    <div class="chip-box">
        <h3 class="chip-box__header">
            Top Genres
        </h3>
           <v-card class="chip-box-card" dark>
            <v-card-text class="chip-box-card__content">
                <v-chip class="chip-box-card__chip" color="primary" :close="true">
                    Horror
                </v-chip>
            </v-card-text>
        </v-card>
    </div>
</template>

<script src="./ChipBox.js" />
<style src="./ChipBox.css" />