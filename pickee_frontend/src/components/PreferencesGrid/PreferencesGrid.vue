<template>
    <div class="preferences-grid">
        <h3 class="preferences-grid-header">{{ boxTitle }}</h3>
        <v-card class="preferences-grid-card" dark>
            <v-card-text>
                <div class="preferences-grid-content">
                    <p v-if="items.length === 0">We don't know your favorites yet. Add some!</p>
                    <div class="preferences-grid-content__block" v-for="item in items" v-bind:key="item.id">
                        <template v-if="type == 'actors'">
                            <v-avatar class="preferences-grid-content__picture" v-if="item.image">
                                <img :src="item.image" :alt="item.text"/>
                            </v-avatar>
                            <div class="preferences-grid-content__empty-avatar" v-else />
                        </template>

                        <template v-if="type == 'movies'">
                            <v-img class="preferences-grid-content__poster" v-if="item.picture">
                                <img :src="item.picture" :alt="item.text" />
                            </v-img>
                            <div class="preferences-grid-content__empty-poster" v-else />
                        </template>
                        
                        <p class="preferences-grid-content__label">{{ item.text }}</p>
                    </div>
                </div>

                <AddItemDialog 
                    :addButtonText="addButtonText" 
                    :items="items"
                    :entries="entries"
                    :addMethod="addMethod"
                    :removeMethod="removeMethod"
                    :searchMethod="searchMethod"
                    :saveMethod="saveMethod"
                    :searchLoading="searchLoading"
                />
            </v-card-text>
        </v-card>
    </div>
</template>

<script src="./PreferencesGrid.js" />
<style src="./PreferencesGrid.css" />