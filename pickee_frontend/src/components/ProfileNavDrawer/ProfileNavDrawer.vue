<template>
    <v-navigation-drawer width="38rem" class="nav-drawer">
        <div class="nav-drawer__logo"><Logo /></div>
        <NavDrawerLinks :links="links" />
        <div class="nav-drawer__logout-btn">
            <v-btn block>Logout</v-btn>
        </div>
        
    </v-navigation-drawer>
</template>

<script src="./ProfileNavDrawer.js" />
<style src="./ProfileNavDrawer.css" />
