<template>
    <div class="recommendation-descr">
        <v-card>
            <v-card-text>
                <div class="recommendation-descr__top">
                    <v-progress-circular
                        class="recommendation-descr__rating"
                        v-if="recommendation.rating > 0"
                        :value="10 * recommendation.rating"
                        rotate="270"
                        width="2.5"
                        color="primary"
                    >{{ recommendation.rating }}</v-progress-circular>
                    <div class="recommendation-descr__heading">
                        <h2 class="recommendation-descr__title">{{ recommendation.name }}</h2>
                        <p class="recommendation-descr__date">{{ recMovieReleaseDate }}</p>
                    </div>
                </div>
                <div class="recommendation-descr__text">
                    <h3 class="recommendation-descr__text-heading">Overview</h3>
                    <p>{{ recommendation.description }}</p>
                </div>
                <div class="recommendation-descr__text">
                    <h3 class="recommendation-descr__text-heading">Featured Crew</h3>
                    <p>
                        <span 
                            class="recommendation-descr__text-item" 
                            v-for="actor in recommendation.cast"
                            v-bind:key="actor.id"
                        >{{ actor.name }}</span>
                    </p>
                </div>
            </v-card-text>
        </v-card>
        <div class="recommendation-descr__actions">
            <button class="action-button" :disabled="isLoading" @click="newRecEvent('REJECTED')">
                <v-icon color="red">{{ iconThumbDown }}</v-icon>
            </button>
            <button class="action-button" :disabled="isLoading" @click="newRecEvent('BOOKMARKED')">
                <v-icon color="primary">{{ iconFavorites }}</v-icon>
            </button>
            <v-dialog v-model="dialog" width="84rem" :persistent="true">
                <template v-slot:activator="{ on }">
                    <button class="action-button" :disabled="isLoading" v-on="on" @click="acceptEvent('ACCEPTED')">
                        <v-icon color="green">{{ iconThumbUp }}</v-icon>
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
                            <div class="pa-12 text-center" v-if="isLoading">
                                <v-progress-circular
                                    :size="70"
                                    :width="5"
                                    color="secondary"
                                    indeterminate
                                ></v-progress-circular>
                            </div>
                            <template v-else>
                                <template v-if="providerList.length > 0">
                                    <p class="recommendation-descr__popup-text"><strong>Yessssss!</strong> Habemus movie. Now go ahead and watch it.</p>
                                    <ItemList :items="providerList" :button-action="openProvider" />
                                </template>
                                <p class="recommendation-descr__popup-text pb-0" v-else>Sorry, but we don't know any available providers for this movie/show :(</p>
                            </template>
                        </v-card-text>
                    </div>
                </v-card>
            </v-dialog>
        </div>
    </div>
</template>

<script src="./RecommendationDescr.js" />
<style src="./RecommendationDescr.css" />
