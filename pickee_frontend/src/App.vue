<template>
    <div id="app">
        <v-app>
            <HelloWorld msg="Welcome to Your FIRST Vue.js App" />
            <v-combobox
                v-model="select"
                :items="items"
                label="Combobox"
                multiple
                chips
            ></v-combobox>

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
        </v-app>
    </div>
</template>

<script>
    import { mdiAccount } from "@mdi/js";
    import HelloWorld from "./components/HelloWorld.vue";

    export default {
        name: "AppOne",
        data() {
            return {
                select: ["Vuetify", "Programming"],
                items: ["Programming", "Design", "Vue", "Vuetify"],
                iconAccount: mdiAccount
            };
        },
        components: {
            HelloWorld
        }
    };
</script>

<style>
    #app {
        color: var(--v-general-base);
        margin-top: 60px;
    }
</style>
