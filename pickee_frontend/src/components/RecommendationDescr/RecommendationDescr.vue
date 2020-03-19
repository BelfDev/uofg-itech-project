<template>
    <div class="recommendation-descr">
        <v-card>
            <v-card-text>
                <div class="recommendation-descr__top">
                    <v-progress-circular
                        class="recommendation-descr__rating"
                        :value="ratingValue"
                        rotate="270"
                        width="2.5"
                        color="primary"
                    >{{ ratingValue }}</v-progress-circular>
                    <div class="recommendation-descr__heading">
                        <h2 class="recommendation-descr__title">Title</h2>
                        <p class="recommendation-descr__date">Release date</p>
                    </div>
                </div>
                <div class="recommendation-descr__text">
                    <h3 class="recommendation-descr__text-heading">Overview</h3>
                    <p>At the height of the First World War, two young British soldiers must cross enemy territory and deliver a message that will stop a deadly attack on hundreds of soldiers.</p>
                </div>
                <div class="recommendation-descr__text">
                    <h3 class="recommendation-descr__text-heading">Featured Crew</h3>
                    <p>
                        <span class="recommendation-descr__text-item">Barry Jenkins</span>
                        <span class="recommendation-descr__text-item">Tarell Alvin McCraney</span>
                    </p>
                </div>
            </v-card-text>
        </v-card>
        <div class="recommendation-descr__actions">
            <button class="action-button">
                <v-icon color="red" size="7.5rem">{{ iconThumbDown }}</v-icon>
            </button>
            <button class="action-button">
                <v-icon color="primary" size="7.5rem">{{ iconFavorites }}</v-icon>
            </button>
            <v-dialog v-model="dialog" width="84rem">
                <template v-slot:activator="{ on }">
                    <button class="action-button" v-on="on">
                        <v-icon color="green" size="7.5rem">{{ iconThumbUp }}</v-icon>
                    </button>
                </template>

                <v-card light>
                    <div class="px-8 py-6 py-p-3 px-p-4">
                        <v-icon
                            class="dialog-close"
                            large
                            color="black"
                            @click="dialog = false"
                            >{{ iconClose }}</v-icon>
                        <v-card-text class="px-12 pb-4 px-p-0">
                            <p class="recommendation-descr__popup-text"><strong>Yessssss!</strong> Habemus movie. Now go ahead and watch it.</p>
                            <ItemList :items="items" :button-action="openProvider" />
                        </v-card-text>
                    </div>
                </v-card>
            </v-dialog>
        </div>
    </div>
</template>

<script src="./RecommendationDescr.js" />
<style src="./RecommendationDescr.css" />
