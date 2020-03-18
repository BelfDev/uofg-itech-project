<template>
    <div class="friends-selector">
        <v-avatar 
            class="friends-selector__selected-item" 
            size="16rem" 
            v-for="friend in selectedFriends" 
            v-bind:key="friend.id"
        >
            <img :src="friend.avatar" :alt="friend.name" />
        </v-avatar>
        
        <v-dialog v-model="dialog" width="100rem">
            <template v-slot:activator="{ on }">
                <v-avatar class="friends-selector__selector" size="16rem" v-on="on">
                    <v-icon class="friends-selector__selector-icon" size="8rem">{{ iconPlus }}</v-icon>
                </v-avatar>
            </template>

            <v-card light>
                <div class="px-8 py-6">
                    <v-icon
                        class="dialog-close"
                        large
                        color="black"
                        @click="dialog = false"
                        >{{ iconClose }}</v-icon
                    >
                    <v-card-text class="friends-selector__popup-content">
                        <div class="friends-selector__popup-header mb-8">
                            <v-avatar size="10rem" v-on="on">
                                <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
                            </v-avatar>
                            <p>Hey Nathan, <strong>add friends</strong> to your movie session by typing their user ids in the list below</p>
                        </div>
                        <v-text-field
                            dark
                            class="mb-8"
                            v-model="first"
                            label="Enter your friend's email"
                            :append-icon="iconPlusCircle"
                            @click:append="testInputAppend"
                            solo
                        ></v-text-field>
                    </v-card-text>

                    <v-card-actions class="dialog-actions text-right">
                        <button class="dialog-actions__button">Done</button>
                    </v-card-actions>
                </div>
            </v-card>
        </v-dialog>

    </div>
</template>

<script src="./FriendsSelector.js" />
<style src="./FriendsSelector.css" />