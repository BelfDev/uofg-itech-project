<template>

    <div class="header-auth">

        <v-btn text rounded class="header-auth">
            <v-avatar size="10rem" @click="overlay = !overlay">
                <img :src="user.picture" :alt="user.name" v-if="user.id" />
                <div class="header-auth__anonymous" v-else>
                    <v-icon size="6rem" color="secondary">{{ iconUser }}</v-icon>
                </div>
            </v-avatar>
        </v-btn>

        <v-overlay
          :absolute="true"
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
                        >{{ iconClose }}
                    </v-icon>
                    <v-card-text class="text-center pa-0">
                        <v-avatar class="mb-6" size="13rem">
                            <img :src="user.picture" :alt="user.name" v-if="user.id" />
                            <div class="header-auth__anonymous" v-else>
                                <v-icon size="10rem" color="secondary">{{ iconUser }}</v-icon>
                            </div>
                        </v-avatar>
                        <h3 v-if="user.name">{{ user.name}}</h3>
                        <p class="body-3 mt-2 mb-8" v-if="user.email">{{ user.email }}</p>
                        <p class="body-3 mt-2 mb-8" v-else>Welcome to <strong>Pickee!</strong></p>
                        <div class="pl-12 pr-12 ml-12 mr-12 pl-p-0 pr-p-0 ml-p-0 mr-p-0">
                            <template v-if="user.id">
                                <v-btn
                                    block
                                    class="mb-4 pl-6 pr-6"
                                    color="primary"
                                    href="/profile/"
                                    >Manage account
                                </v-btn>
                                <v-btn block outlined href="/logout/">Logout</v-btn>
                            </template>
                            <template v-else>
                                <v-btn
                                    block
                                    class="mb-4"
                                    color="primary"
                                    href="/login/"
                                    >Login
                                </v-btn>
                                <v-btn class="pl-6 pr-6" block outlined href="/signup/">Create account</v-btn>
                            </template>
                        </div>
                    </v-card-text>
                </div>
            </v-card>
        </v-overlay>

    </div>

</template>

<script src="./HeaderAuth.js" />
<style src="./HeaderAuth.css" />