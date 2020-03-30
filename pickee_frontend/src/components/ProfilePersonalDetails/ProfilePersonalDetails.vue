<template>
    <div class="content-card-box">
        <h3 class="content-card-box__header">Personal details</h3>
        <v-card dark>
            <v-card-text>
                <FormTextField 
                    type="text" 
                    label="First name" 
                    name="first_name" 
                    placeholder="Enter first name"
                    :value="first_name"
                    :changeEvent="updatePersonalDetails" 
                    class="mb-4 mb-p-8" 
                    horizontal
                />
                
                <FormTextField 
                    type="text" 
                    label="Last name" 
                    name="last_name" 
                    placeholder="Enter last name"
                    :value="last_name"
                    :changeEvent="updatePersonalDetails" 
                    class="mb-4 mb-p-8" 
                    horizontal
                />

                <FormDropdownField 
                    :changeEvent="updatePersonalDetails" 
                    label="Age" 
                    name="age" 
                    :value="user.age" 
                    title="Select age" 
                    :items="ageDropdownItems" 
                    class="mb-4 mb-p-8" 
                />

                <FormDropdownField 
                    :changeEvent="updatePersonalDetails" 
                    label="Gender" 
                    name="gender" 
                    :value="user.gender" 
                    :items="genderDropdownItems" 
                    title="Select gender" 
                />
            </v-card-text>
        </v-card> 
    </div>
</template>

<script src="./ProfilePersonalDetails.js" />
<style src="./ProfilePersonalDetails.css" />
