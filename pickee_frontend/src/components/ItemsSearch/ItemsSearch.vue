<template>
    <div class="items-search">
        <SearchSuggestions 
            :entries="entries" 
            :addMethod="addMethod" 
            :searchMethod="searchMethod" 
            :searchLoading="searchLoading" 
        />
        <ItemList :items="items" :button-action="removeMethod" />
    </div>
</template>

<script src="./ItemsSearch.js" />
<style src="./ItemsSearch.css" />
