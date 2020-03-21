<template>
    <div class="genre-preferences mt-12">
        <h3 class="image-grid-header">Favorite genres</h3>
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
</template>

<script src="./GenrePreferences.js" />
<style src="./GenrePreferences.css" />
