<template>
    <ul class="item-list">
        <template v-for="item in items">
            <li class="item-list__element" v-bind:key="item.id">
                <button @click="buttonAction(item)" class="item-list__element-button">
                    <v-avatar class="item-list__element-avatar" size="6.8rem" v-if="item.image">
                        <img :src="item.image" :alt="item.text" />
                    </v-avatar>
                    <img class="item-list__element-picture" :src="item.picture" :alt="item.text" v-else-if="item.picture" />
                    <div class="item-list__element-logo" v-if="item.logo"><img :src="item.logo" :alt="item.text" /></div>
                    <span class="item-list__element-text">{{ item.text }}</span>
                    <span class="item-list__element-type" v-if="item.type">{{ item.type }}</span>
                    <v-icon class="item-list__element-icon" v-if="item.icon">{{ item.icon }}</v-icon>
                </button>
            </li>
        </template>
    </ul>
    
</template>
 
<script src="./ItemList.js" />
<style src="./ItemList.css" />