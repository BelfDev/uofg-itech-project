<template>
    <div id="app">
        <v-app>
            <v-content>
                <h1>Heading 1</h1>
                <h2>Heading 2</h2>

                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua
                </p>
                <p class="body-4">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua
                </p>
                <p class="body-2">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua
                </p>
                <p class="body-1">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua
                </p>

                <v-card class="mb-6 pa-6" light>
                    <v-btn outlined>Logout</v-btn>
                </v-card>

                <div class="mb-6">
                    <v-btn>Logout</v-btn>
                </div>

                <div class="mb-6">
                    <v-btn color="primary">Add actor</v-btn>
                </div>

                <div class="mb-6">
                    <v-btn large color="primary">Search</v-btn>
                </div>

                <v-btn rounded x-large color="primary"
                    >Pick a movie for me
                    <v-icon class="ml-5" size="56">{{
                        iconArrowRight
                    }}</v-icon></v-btn
                >
            </v-content>
        </v-app>
    </div>
</template>

<script>
    import { mdiChevronRight } from "@mdi/js";

    export default {
        name: "AppOne",
        data: () => ({
            iconArrowRight: mdiChevronRight
        }),
        components: {}
    };
</script>

<style>
    #app {
        margin: 20px;
    }
</style>
