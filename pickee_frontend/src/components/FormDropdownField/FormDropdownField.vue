<template>
    <div class="form-dropdown-field">
        <label class="label">{{ label }}</label>
        <v-select
            :items="items"
            filled
            :single-line="false"
            :value="value"
            :label="title"
            @change="changeEvent"
        >
        </v-select>
    </div>
</template>

<script src="./FormDropdownField.js" />
<style src="./FormDropdownField.css" />

