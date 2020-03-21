<template>
    <div class="image-grid">
        <h3 class="image-grid-header">Favorite Movies</h3>
        <v-card class="image-grid-card" dark>
            <v-card-text>
                <div class="image-grid-content">
                    <div class="image-grid-content__poster-box" v-for="item in items" v-bind:key="item.id">
                        <v-img class="image-grid-content__poster">
                            <img :src="item.picture" :alt="item.text" />
                        </v-img>
                        <p class="image-grid-content__label">{{ item.text }}</p>
                    </div>
                </div>

                <v-dialog v-model="dialog" width="100rem">
                    <template v-slot:activator="{ on }">
                        <div class="image-grid-content__btn" v-on="on">
                            <v-btn color="primary">Add movie</v-btn>
                        </div>
                    </template>

                    <v-card light>
                        <div class="px-8 py-6 px-p-4 py-p-3">
                            <v-icon
                                class="dialog-close"
                                large
                                color="black"
                                @click="dialog = false"
                                >{{ iconClose }}</v-icon>
                            <v-card-text class="image-grid__popup-content image-grid__popup-content">
                                <div class="image-grid__search-box">
                                    <v-text-field
                                        dark
                                        class="image-grid__search-input"
                                        :prepend-icon="iconSearch"
                                        solo
                                    ></v-text-field>
                                    <v-btn color="primary" large class="image-grid__search-btn">Search</v-btn>
                                </div>
                                <ItemList :items="items" :button-action="removeItem" />
                            </v-card-text>
                        </div>
                    </v-card>
                </v-dialog>
             
            </v-card-text>
        </v-card>
    </div>
</template>

<script src="./MovieGrid.js" />
<style src="./MovieGrid.css" />
