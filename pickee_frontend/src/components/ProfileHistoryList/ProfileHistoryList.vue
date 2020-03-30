<template>
    <div class="history-list-wrapper">
    <h3 class="history-list__header">Recommendation History</h3>
        <ul class="history-list">
            <template v-for="(item, index) in historyItems">
                <li class="history-list__element" v-bind:key="index + item.text">
                    <v-img v-if="item.image" class="history-list__element-poster" :contain="false" max-width="10rem" >
                        <img :src="item.image" :alt="item.text" />
                    </v-img>
                    <div class="history-list__empty-poster" v-else><span>Poster not yet available</span></div>
                    <span class="history-list__element-text">{{ item.text }}</span>
                    <div class="action-button history-list__element-icon" v-if="item.icon">
                        <v-icon :color="item.color" size="3.5rem">{{ item.icon }}</v-icon>
                    </div>
                </li>
            </template>
        </ul>
    </div>
</template>

<script src="./ProfileHistoryList.js" />
<style src="./ProfileHistoryList.css" />
