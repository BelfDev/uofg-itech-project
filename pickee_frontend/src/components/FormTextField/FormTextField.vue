<template>
    <div class="form-text-field" :class="{ 'form-text-field--horizontal': horizontal }">
        <label class="label">{{ label }}</label>
        <v-text-field 
            v-model="model" 
            :placeholder="placeholder" 
            :name="name" 
            :type="type" 
            @change="changeEvent && changeEvent(name, model)"
            solo 
            dark
        ></v-text-field>
    </div>
</template>

<script src="./FormTextField.js" />
<style src="./FormTextField.css" />

