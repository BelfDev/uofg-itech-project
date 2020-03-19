<template>
    <v-app>
        <v-content>
            <h1>Hello, 
                <span v-if="user" class="heading1-accent">{{ user.name }}</span>
                <span v-else class="heading1-accent">guest</span>
            </h1>
            <h2>Heading 2</h2>

            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua
            </p>
            <p class="body-4">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua
            </p>
            <p class="body-2">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua
            </p>
            <p class="body-1">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua
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

                <v-btn rounded x-large color="primary">
                    Pick a movie for me
                    <v-icon class="ml-5" size="5.6rem">{{ iconArrowRight }}</v-icon>
                </v-btn>
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
                        item-color="white"
                        solo
                        multiple
                        chips
                        ><template v-slot:selection="data">
                            <v-chip
                                color="primary"
                                :key="JSON.stringify(data.item)"
                                v-bind="data.attrs"
                                :input-value="data.selected"
                                :disabled="data.disabled"
                                @click:close="data.parent.selectItem(data.item)"
                            >
                                {{ data.item }}
                            </v-chip>
                        </template></v-combobox
                    >
                </div>
                <div class="mb-6">
                    <TimeSlider />
                </div>
            </div>

            <div class="mb-10">
                <v-dialog v-model="dialog" width="500">
                    <template v-slot:activator="{ on }">
                        <v-btn color="primary" v-on="on">
                            Click Me
                        </v-btn>
                    </template>

                    <v-card light>
                        <div class="pa-6">
                            <v-icon
                                class="dialog-close"
                                large
                                color="black"
                                @click="dialog = false"
                                >{{ iconClose }}</v-icon
                            >
                            <v-card-text class="mt-6">
                                Lorem ipsum dolor sit amet, consectetur
                                adipiscing elit, sed do eiusmod tempor
                                incididunt ut labore et dolore magna aliqua. Ut
                                enim ad minim veniam, quis nostrud exercitation
                                ullamco laboris nisi ut aliquip ex ea commodo
                                consequat.
                            </v-card-text>

                            <v-card-actions class="dialog-actions">
                                <div class="mb-4">
                                    <v-btn
                                        block
                                        color="primary"
                                        @click="dialog = false"
                                        >Manage account
                                    </v-btn>
                                </div>
                                <v-btn block outlined>Logout </v-btn>
                            </v-card-actions>
                        </div>
                    </v-card>
                </v-dialog>
            </div>

            <div>
                <v-avatar size="10rem">
                    <img
                        src="https://cdn.vuetifyjs.com/images/john.jpg"
                        alt="John"
                    />
                </v-avatar>
            </div>
        </v-content>
    </v-app>
</template>

<script>
    import { mdiChevronRight, mdiPlusCircle, mdiClose } from "@mdi/js";
    import TimeSlider from "@/components/TimeSlider/TimeSlider.vue";

    export default {
        name: "Demo",
        data: () => ({
            user: window.user,
            dialog: false,
            first: "belfdev@gmail.com",
            select: ["Vuetify", "Programming"],
            items: ["Programming", "Design", "Vue", "Vuetify"],
            iconClose: mdiClose,
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
