<template>
    <form class="casual-prefences-selection" :action="urls.recommendation" method="POST">
        <input type="hidden" name="csrfmiddlewaretoken" :value="token">

        <div class="casual-prefences-selection__wrapper">
            <div class="casual-prefences-selection__form">
                <div class="mb-12 pt-6 pt-p-0">
                    <label class="label-accented mb-8">How much time you got?</label>
                    <TimeSlider name="runtime" />
                </div>
                <div class="mb-10 pt-6 pt-p-0 mb-p-0">
                    <label class="label-accented mb-8">Any genres in mind?</label>
                    <input type="hidden" name="genre_ids" v-model="genreValue" />
                    <v-select
                        v-model="selectedGenres"
                        :items="items"
                        :menu-props="{ zIndex: 1000 }"
                        label="Select genres"
                        item-color="white"
                        item-value="text"
                        :return-object="false"
                        @change="updateGenreValue"
                        solo
                        multiple
                        chips
                    >
                        <template v-slot:selection="data">
                            <v-chip
                                color="primary"
                                text-color="secondary"
                                :key="JSON.stringify(data.item)"
                                v-bind="data.attrs"
                                :disabled="data.disabled"
                            >
                                {{ data.item.text }}
                            </v-chip>
                        </template>
                    </v-select>
                </div>
                <div>
                    <label class="label-accented mb-8">Got yourself company?</label>
                    <SessionUserSelector :urls="urls" :user="user" />
                </div>
            </div>
            <div class="casual-prefences-selection__action-block">
                <button type="submit" class="casual-prefences-selection__action-btn">
                    <v-icon class="casual-prefences-selection__action-icon">{{iconPlay}}</v-icon>
                </button>
            </div>
        </div>
    </form>
</template>

<script src="./CasualPreferencesSelection.js" />
<style src="./CasualPreferencesSelection.css" />
