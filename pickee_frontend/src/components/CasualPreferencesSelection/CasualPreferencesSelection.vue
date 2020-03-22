<template>
    <form class="casual-prefences-selection" action="recommendation/" method="POST">
        <input type="hidden" name="csrfmiddlewaretoken" :value="token">
        <div class="casual-prefences-selection__wrapper">
            <div class="casual-prefences-selection__form">
                <div class="mb-12 pt-6">
                    <label class="label-accented mb-8">How much time you got?</label>
                    <TimeSlider name="runtime" />
                </div>
                <div class="mb-10 pt-6">
                    <label class="label-accented mb-8">Any genres in mind?</label>
                    <input type="hidden" name="genres" v-model="genreValue" />
                    <v-combobox
                        v-model="selectedGenres"
                        :items="items"
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
                                :key="JSON.stringify(data.item)"
                                v-bind="data.attrs"
                                :disabled="data.disabled"
                            >
                                {{ data.item }}
                            </v-chip>
                        </template>
                    </v-combobox>
                </div>
                <div>
                    <label class="label-accented mb-8">Got yourself a company?</label>
                    <FriendsSelector :user="user" />
                </div>
            </div>
            <div class="casual-prefences-selection__action-block">
                <button type="submit" class="casual-prefences-selection__action-btn">
                    <v-icon class="casual-prefences-selection__action-icon" size="33rem">{{iconPlay}}</v-icon>
                </button>
            </div>
        </div>
    </form>
</template>

<script src="./CasualPreferencesSelection.js" />
<style src="./CasualPreferencesSelection.css" />
