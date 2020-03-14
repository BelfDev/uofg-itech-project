<template>
    <v-navigation-drawer class="nav-drawer">
        <div class="nav-drawer__logo"><Logo /></div>
        <div class="nav-drawer-links">
            <a class="nav-drawer-links__item nav-drawer-links__item--active" href="/profile/">
                <v-icon class="mr-3">{{ iconProfile }}</v-icon>
                Profile
            </a>
            <a class="nav-drawer-links__item" href="/preferences/">
                <v-icon class="mr-3">{{ iconPreferences }}</v-icon>
                Preferences
            </a>
            <a class="nav-drawer-links__item" href="/history/">
                <v-icon class="mr-3">{{ iconHistory }}</v-icon>
                History
            </a>
        </div>

        <div class="nav-drawer__logout-btn">
            <v-btn block>Logout</v-btn>
        </div>
        
    </v-navigation-drawer>
</template>

<script src="./ProfileNavDrawer.js" />
<style src="./ProfileNavDrawer.css" />
