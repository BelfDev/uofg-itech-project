<template>
    <ul class="item-list">
        <template v-for="item in items">
            <li class="item-list__element" v-bind:key="item.text">
                <v-avatar class="item-list__element-avatar" size="6.8rem">
                <img :src="item.image" :alt="item.text" />
                </v-avatar>
                <span class="item-list__element-text">{{ item.text }}</span>
                <v-icon class="item-list__element-icon">{{ item.icon }}</v-icon>
            </li>
        </template>
    </ul>
    
</template>
 
<script src="./ItemList.js" />
<style src="./ItemList.css" />