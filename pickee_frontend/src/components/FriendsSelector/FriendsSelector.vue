<template>
    <div class="friends-selector">
        <div class="friends-selector__selected">
            <v-avatar 
                class="friends-selector__selected-item" 
                size="16rem"
                v-for="friend in selectedFriends"
                v-bind:key="friend.id"
            >
                <img :src="friend.image" :alt="friend.name" />
            </v-avatar>
        </div>
        
        <v-dialog v-model="dialog" :width="user ? '100rem' : '64rem'">
            <template v-slot:activator="{ on }">
                <v-avatar class="friends-selector__selector" size="16rem" v-on="on">
                    <v-icon class="friends-selector__selector-icon" size="8rem">{{ iconPlus }}</v-icon>
                </v-avatar>
            </template>

            <v-card light v-if="user">
                <div class="px-8 py-6 px-p-4 py-p-3">
                    <v-icon
                        class="dialog-close"
                        large
                        color="black"
                        @click="dialog = false"
                        >{{ iconClose }}</v-icon>
                    <v-card-text class="friends-selector__popup-content pb-4">
                        <div class="friends-selector__popup-header mb-8">
                            <v-avatar size="10rem">
                                <img :src="user.picture" :alt="user.name" />
                            </v-avatar>
                            <p>Hey {{ user.name }}, <strong>add friends</strong> to your movie session by typing their user ids in the list below</p>
                        </div>
                        <v-text-field
                            dark
                            v-model="friendEmail"
                            label="Enter your friend's email"
                            :append-icon="iconPlusCircle"
                            @click:append="addFriend"
                            solo
                        ></v-text-field>
                        <ItemList :items="selectedFriends" :button-action="removeFriend" />
                    </v-card-text>

                    <v-card-actions class="dialog-actions text-right">
                        <button class="dialog-actions__button" @click="dialog = false">Done</button>
                    </v-card-actions>
                </div>
            </v-card>

            <v-card light v-else>
                <div class="px-8 py-6 px-p-4 py-p-3">
                    <v-icon
                        class="dialog-close"
                        large
                        color="black"
                        @click="dialog = false"
                        >{{ iconClose }}</v-icon>
                    <v-card-text class="friends-selector__popup-content friends-selector__popup-content--unauthorized pb-4">
                        <div class="friends-selector__popup-header mb-10">
                            <v-avatar size="10rem">
                                <v-icon size="8rem" color="black">{{ iconUser }}</v-icon>
                            </v-avatar>
                            <p><strong>Uh-oh!</strong> Looks like you are logged out.</p>
                        </div>
                        <p class="mb-12">Please log in to invite friends to your movie session.</p>
                        <div class="pl-12 pr-12 ml-12 mr-12 pl-p-0 pr-p-0 ml-p-0 mr-p-0">
                            <v-btn
                                block
                                class="mb-4 pl-6 pr-6"
                                color="primary"
                                >Login
                            </v-btn>
                            <v-btn class="mb-4 pl-6 pr-6" block outlined>Create account </v-btn>
                        </div>
                    </v-card-text>
                </div>
            </v-card>
        </v-dialog>

    </div>
</template>

<script src="./FriendsSelector.js" />
<style src="./FriendsSelector.css" />