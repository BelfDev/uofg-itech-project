<template>
    <div class="content-card-box">
        <h3 class="content-card-box__header">Personal details</h3>
        <v-card dark>
            <v-card-text>
                <FormDropdownField label="Age" name="age" title="Select age" :items="ageDropdownItems" class="mb-4" />
                <FormDropdownField label="Gender" name="gender" :items="genderDropdownItems" title="Select gender" />
            </v-card-text>
        </v-card> 
    </div>
</template>

<script src="./ProfilePersonalDetails.js" />
<style src="./ProfilePersonalDetails.css" />
