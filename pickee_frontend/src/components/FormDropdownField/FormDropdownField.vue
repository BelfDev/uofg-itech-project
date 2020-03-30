<template>
    <div class="form-dropdown-field">
        <label class="label">{{ label }}</label>
        <v-select
            :items="items"
            filled
            :name="name"
            v-model="model"
            :single-line="false"
            :label="title"
            @change="changeEvent(name, model)"
        >
        </v-select>
    </div>
</template>

<script src="./FormDropdownField.js" />
<style src="./FormDropdownField.css" />

