<template>

    <div class="header-auth">

        <v-avatar class="header-auth" size="10rem" @click="overlay = !overlay">
            <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
        </v-avatar>

        <v-overlay
          absolute="true"
          color=""
          :value="overlay"
        >
            <v-card light>
                <div class="pa-6">
                    <v-icon
                        class="dialog-close"
                        large
                        color="black"
                        @click="overlay = false"
                        >{{ iconClose }}</v-icon
                    >
                    <v-card-text class="text-center pa-0">
                        <v-avatar class="mb-6" size="13rem" v-on="on">
                            <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
                        </v-avatar>
                        <h3>Nathan</h3>
                        <p class="body-3 mt-2 mb-8">nathan.nerdy@gmail.com</p>
                        <div class="pl-12 pr-12 ml-12 mr-12">
                            <v-btn
                                block
                                class="mb-4 pl-6 pr-6"
                                color="primary"
                                @click="dialog = false"
                                >Manage account
                            </v-btn>
                            <v-btn block outlined>Logout </v-btn>
                        </div>
                    </v-card-text>
                </div>
            </v-card>
        </v-overlay>

    </div>

</template>

<script src="./HeaderAuth.js" />
<style src="./HeaderAuth.css" />