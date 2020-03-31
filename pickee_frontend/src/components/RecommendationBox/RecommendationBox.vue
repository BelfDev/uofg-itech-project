<template>
    <div class="recommendation-box" :class="{'recommendation-box--loading' : isLoading}">
        <v-btn color="secondary" class="recommendation-box__goback" href="/?step=2">Back to preferences</v-btn>
        <div class="mx-auto mt-p-12 recommendation-box__loader" v-if="isInitialLoading || isLoading">
            <v-progress-circular
                :size="140"
                :width="7"
                color="primary"
                indeterminate
            ></v-progress-circular>
        </div>

        <template v-if="!isInitialLoading && recData.id">
            <RecommendationCarousel 
                ref="recCarousel" 
                :activeSlideIndex="activeRecIndex"
                :recommendation="recData" 
                :isLoading="isLoading" 
                :showPrevRec="showPrevRec"
                :showNextRec="showNextRec"
            />
            <RecommendationDescr 
                :user="user"
                :recommendation="recData" 
                :providerList="providerList"
                :newRecEvent="getNewRecommendation" 
                :acceptEvent="getProviderList" 
                :isLoading="isLoading"
            />
        </template>

        <v-dialog v-model="noResultsDialog" width="84rem" :persistent="true">
            <v-card light>
                <div class="px-8 py-6 py-p-3 px-p-4">
                    <v-icon
                        class="dialog-close"
                        large
                        color="black"
                        @click="noResultsDialog = false"
                        >{{ iconClose }}</v-icon>
                    <v-card-text class="pt-12 my-12 py-12 px-p-0">
                        <h3 class="pt-6 mb-6 text-center">Whoaaaah! You are too pickee. You should come and work for us.</h3>
                        <p class="">Unfortunately your preferences are a bit too narrow, please come back and edit them to get fresh recommendations :)</p>
                    </v-card-text>

                    <v-card-actions class="dialog-actions d-flex justify-space-between">
                        <button class="dialog-actions__button" @click="navigateBackToHome">Return to home page</button>
                        <button class="dialog-actions__button" v-if="recData" @click="noResultsDialog = false;">Done</button>
                    </v-card-actions>
                </div>
            </v-card>
        </v-dialog>
    </div>
</template>

<script src="./RecommendationBox.js" />
<style src="./RecommendationBox.css" />
