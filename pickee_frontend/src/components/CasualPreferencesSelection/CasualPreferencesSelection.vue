<template>
    <div class="casual-prefences-selection">
        <div class="mb-6">
            <label class="label">How much time you got?</label>
            <TimeSlider />
        </div>
        <div class="mb-6">
            <label class="label">Any genres in mind?</label>
            <v-combobox
                v-model="select"
                :items="items"
                label="Select genres from this list"
                item-color="white"
                solo
                multiple
                chips
                ><template v-slot:selection="data">
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
            <label class="label">Got yourself a company?</label>
            <div>Add friend</div>
        </div>
    </div>
</template>

<script src="./CasualPreferencesSelection.js" />
<style src="./CasualPreferencesSelection.css" />
