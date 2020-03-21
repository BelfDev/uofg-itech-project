<template>
    <div class="history-list-wrapper">
    <h3 class="history-list__header">Recommendation History</h3>
        <ul class="history-list">
            <template v-for="item in historyItems">
                <li class="history-list__element" v-bind:key="item.text">
                    <v-img class="history-list__element-poster" :contain="false" max-width="5.4rem" max-height="6.8rem" >
                        <img :src="item.image" :alt="item.text" />
                    </v-img>
                    <span class="history-list__element-text">{{ item.text }}</span>
                    <div class="action-button history-list__element-icon">
                        <v-icon :color="item.color" size="3.5rem">{{ item.icon }}</v-icon>
                    </div>
                </li>
            </template>
        </ul>
    </div>
</template>

<script src="./ProfileHistoryList.js" />
<style src="./ProfileHistoryList.css" />
