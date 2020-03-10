<template>
    <div id="app">
        <v-app>
            <TestComponent />

            <h1>Heading 1</h1>
            <h2>Heading 2</h2>

            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua
            </p>
            <p class="text-small">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua
            </p>
            <p class="text-medium">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua
            </p>
            <p class="text-large">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua
            </p>

            <v-card>
                <v-card-text>
                    <v-icon>{{ iconAccount }}</v-icon> Test

                    <div
                        style="display: flex; justify-content: space-between; margin-top: 20px;"
                    >
                        <v-btn rounded color="primary" dark>
                            <v-icon>{{ iconAccount }}</v-icon
                            >Rounded Button</v-btn
                        >

                        <v-btn rounded large color="primary" dark>
                            <v-icon>{{ iconAccount }}</v-icon
                            >Rounded Button</v-btn
                        >
                    </div>
                </v-card-text>
            </v-card>
        </v-app>
    </div>
</template>

<script>
    import { mdiAccount } from "@mdi/js";
    import TestComponent from "./components/TestComponent.vue";

    export default {
        name: "AppOne",
        data: () => ({
            iconAccount: mdiAccount
        }),
        components: {
            TestComponent
        }
    };
</script>

<style>
    #app {
        margin: 20px;
    }
</style>
