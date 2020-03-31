<template>
    <div>
        <v-btn class="nav-drawer-activator" icon color="white" v-if="!drawer" @click="drawer = true">
            <v-icon>{{ iconMenu }}</v-icon>
        </v-btn>
        <v-navigation-drawer 
            width="38rem" 
            class="nav-drawer" 
            fixed
            v-model="drawer" 
            :mobile-break-point="drawer ? 0 : 1024"
        >
            <div class="nav-drawer__logo"><Logo /></div>
            <NavDrawerLinks :links="links" />
            <div class="nav-drawer__logout-btn">
                <v-btn block :href="logoutUrl">Logout</v-btn>
            </div>
            
        </v-navigation-drawer>
    </div>
</template>

<script src="./ProfileNavDrawer.js" />
<style src="./ProfileNavDrawer.css" />
