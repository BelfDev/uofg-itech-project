<template>
    <div class="image-grid">
        <h3 class="image-grid-header">Favorite Actors</h3>
        <v-card class="image-grid-card" dark>
            <v-card-text>
                <div class="image-grid-content">
                    <div class="image-grid-content__block" v-for="item in items" v-bind:key="item.id">
                        <v-avatar class="image-grid-content__picture" size="13.4rem">
                            <img :src="item.image" :alt="item.text"/>
                        </v-avatar>
                        <p class="image-grid-content__label">{{ item.text }}</p>
                    </div>
                </div>

                <v-dialog v-model="dialog" width="100rem">
                    <template v-slot:activator="{ on }">
                        <div class="image-grid-content__btn" v-on="on">
                            <v-btn color="primary">Add actor</v-btn>
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
                                        v-model="searchText"
                                        class="image-grid__search-input"
                                        :prepend-icon="iconSearch"
                                        solo
                                    ></v-text-field>
                                    <v-btn color="primary" large class="image-grid__search-btn" @click="addMethod(searchText)">Search</v-btn>
                                </div>
                                <ItemList :items="items" :button-action="removeMethod" />
                            </v-card-text>
                        </div>
                    </v-card>
                </v-dialog>
             
            </v-card-text>
        </v-card>
    </div>
</template>

<script src="./ActorGrid.js" />
<style src="./ActorGrid.css" />
