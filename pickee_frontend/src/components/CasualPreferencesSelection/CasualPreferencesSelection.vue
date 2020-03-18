<template>
    <div class="casual-prefences-selection">
        <div class="casual-prefences-selection__form">
            <div class="mb-12 pt-6">
                <label class="label-accented mb-8">How much time you got?</label>
                <TimeSlider />
            </div>
            <div class="mb-10 pt-6">
                <label class="label-accented mb-8">Any genres in mind?</label>
                <v-combobox
                    v-model="select"
                    :items="items"
                    label="Select genres from this list"
                    item-color="white"
                    solo
                    multiple
                    chips
                    >
                    <template v-slot:selection="data">
                        <v-chip
                            color="primary"
                            :key="JSON.stringify(data.item)"
                            v-bind="data.attrs"
                            :input-value="data.selected"
                            :disabled="data.disabled"
                            @click:close="data.parent.selectItem(data.item)"
                        >
                            {{ data.item }}
                        </v-chip>
                    </template>
                </v-combobox>
            </div>
            <div>
                <label class="label-accented mb-8">Got yourself a company?</label>
                <FriendsSelector />
            </div>
        </div>
        <div class="casual-prefences-selection__action-block">
            <button class="casual-prefences-selection__action-btn">
                <v-icon class="casual-prefences-selection__action-icon" size="33rem">{{iconPlay}}</v-icon>
            </button>
        </div>
    </div>
</template>

<script src="./CasualPreferencesSelection.js" />
<style src="./CasualPreferencesSelection.css" />
