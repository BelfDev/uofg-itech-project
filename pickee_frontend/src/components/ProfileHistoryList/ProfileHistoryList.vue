<template>
    <div class="history-list-wrapper">
    <h3 class="history-list__header">Recommendation History</h3>
        <ul class="history-list">
            <template v-for="item in items">
                <li class="history-list__element" v-bind:key="item.text">
                    <v-img class="history-list__element-poster" :contain="false" :max-width="54" :max-height="68" >
                        <img :src="item.image" :alt="item.text" />
                    </v-img>
                    <span class="history-list__element-text">{{ item.text }}</span>
                    <v-icon class="history-list__element-icon">{{ item.icon }}</v-icon>
                </li>
            </template>
        </ul>
    </div>
</template>

<script src="./ProfileHistoryList.js" />
<style src="./ProfileHistoryList.css" />
