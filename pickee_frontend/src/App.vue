<template>
    <div id="app">
        <HelloWorld msg="Welcome to Your FIRST Vue.js App" />
        <v-card>
            <v-icon>{{ iconAccount }}</v-icon> Test
            <br />
            <v-btn rounded color="primary" dark>
                <v-icon>{{ iconAccount }}</v-icon
                >Rounded Button</v-btn
            >
            <br />
            <v-btn rounded large color="primary" dark>
                <v-icon>{{ iconAccount }}</v-icon
                >Rounded Button</v-btn
            >
        </v-card>
    </div>
</template>

<script>
    import { mdiAccount } from "@mdi/js";
    import HelloWorld from "./components/HelloWorld.vue";

    export default {
        name: "AppOne",
        data: () => ({
            iconAccount: mdiAccount
        }),
        components: {
            HelloWorld
        }
    };
</script>

<style>
    #app {
        color: var(--v-secondary-base);
        margin-top: 60px;
    }
</style>
