<template>
    <div class="nav-drawer-links">
        <template 
            v-for="link in links" 
        >
            <a
                class="nav-drawer-links__item"
                :href="link.url"
                :class="{ 'nav-drawer-links__item--active': isActive(link.url) }"
                v-bind:key="link.url"
            >
                <v-icon class="mr-3">{{ link.icon }}</v-icon>
                {{ link.name}}
            </a>
        </template>
    </div>
</template>

<script src="./NavDrawerLinks.js" />
<style src="./NavDrawerLinks.css" />
