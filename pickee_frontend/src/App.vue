<template>
    <div id="app">
        <v-app>
            <v-content>
                <h1>Feeling <span class="heading1-accent">Pickee?</span></h1>
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

                <div class="mb-10">
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
                </div>

                <div>
                    <div class="mb-6">
                        <v-text-field
                            v-model="first"
                            label="First Name"
                            :append-icon="iconPlus"
                            @click:append="testInputAppend"
                            solo
                        ></v-text-field>
                    </div>
                    <div class="mb-6">
                        <label class="label">Any genres in mind?</label>
                        <v-combobox
                            v-model="select"
                            :items="items"
                            label="Select genres from this list"
                            solo
                            multiple
                            chips
                        ></v-combobox>
                    </div>
                    <div class="mb-6">
                        <TimeSlider />
                    </div>
                </div>
            </v-content>
        </v-app>
    </div>
</template>

<script>
    import { mdiChevronRight, mdiPlusCircle } from "@mdi/js";
    import TimeSlider from "./components/TimeSlider/TimeSlider.vue";

    export default {
        name: "AppOne",
        data: () => ({
            first: "belfdev@gmail.com",
            iconPlus: mdiPlusCircle,
            iconArrowRight: mdiChevronRight
        }),
        methods: {
            testInputAppend: function() {
                console.log("testInputAppend");
            }
        },
        components: {
            TimeSlider
        }
    };
</script>

<style>
    #app {
        margin: 20px;
    }
</style>
