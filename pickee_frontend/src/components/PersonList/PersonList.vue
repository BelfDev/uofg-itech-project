<template>
    <div class="person-list">
        <template v-for="developer in developers">
            <Person 
                v-bind:key="developer"
                :name="developer.name" 
                :role="developer.role" 
                :avatar="developer.avatar" />
        </template>
    </div>
</template>

<script src="./PersonList.js" />
<style src="./PersonList.css" />