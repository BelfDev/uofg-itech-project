<template>
    <div class="search-suggestions" :class="{ 'search-suggestions--loading' : searchLoading }">
        <v-menu :value="entries || undefined" :disabled="!entries" allow-overflow max-height="26rem" offset-y>
            <template v-slot:activator="{ on }">
                <div class="search-suggestions__search-box" ref="searchInput" v-on="on">
                    <v-text-field
                        dark
                        v-model="searchText"
                        class="search-suggestions__search-input"
                        :prepend-icon="iconSearch"
                        @keydown="searchEvent"
                        solo
                    ></v-text-field>
                    <v-btn 
                        color="primary" 
                        large 
                        class="search-suggestions__search-btn" 
                        @click="searchEvent"
                    >Search</v-btn>
                </div>
            </template>
            <v-list v-if="entries && entries.length > 0">
                <v-list-item
                    v-for="(item, index) in entries"
                    :disabled="isAlreadyAdded(item)"
                    :key="index"
                    @click="addEvent(item, index)"
                >
                    <v-list-item-avatar>
                        <v-img :src="item.image_url" v-if="item.image_url"></v-img>
                        <v-icon v-else>{{ iconUser }}</v-icon>
                    </v-list-item-avatar>
                    <v-list-item-content>
                        <v-list-item-title v-text="item.name"></v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
            <v-list v-else>
                <v-list-item>No actors found</v-list-item>
            </v-list>
        </v-menu>
    </div>
</template>

<script src="./SearchSuggestions.js" />
<style src="./SearchSuggestions.css" />

