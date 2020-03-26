<template>
    <div class="session-user-selector">
        <input type="hidden" name="user_ids" :value="userIDs" />
        <div class="session-user-selector__selected">
            <v-avatar 
                class="session-user-selector__selected-item" 
                size="16rem"
                v-for="friend in selectedFriends"
                v-bind:key="friend.id"
            >
                <img :src="friend.image" :alt="friend.name" v-if="friend.picture" />
                <v-icon size="8rem" color="white" :title="friend.name" v-else>{{ iconUser }}</v-icon>
            </v-avatar>
        </div>
        
        <v-dialog v-model="dialog" :width="user.id ? '100rem' : '64rem'">
            <template v-slot:activator="{ on }">
                <v-avatar class="session-user-selector__selector" size="16rem" v-on="on">
                    <v-icon class="session-user-selector__selector-icon" size="8rem">{{ iconPlus }}</v-icon>
                </v-avatar>
            </template>

            <v-card light v-if="user.id">
                <div class="px-8 py-6 px-p-4 py-p-3">
                    <v-icon
                        class="dialog-close"
                        large
                        color="black"
                        @click="dialog = false"
                        >{{ iconClose }}</v-icon>
                    <v-card-text class="session-user-selector__popup-content pb-4">
                        <div class="session-user-selector__popup-header mb-8">
                            <v-avatar size="10rem">
                                <img :src="user.picture" :alt="user.name" v-if="user.picture" />
                                <v-icon size="6rem" color="secondary" v-else>{{ iconUser }}</v-icon>
                            </v-avatar>
                            <p>Hey {{ user.name }}, <strong>add friends</strong> to your movie session by typing their user ids in the list below</p>
                        </div>
                        <v-text-field
                            dark
                            v-model="friendEmail"
                            label="Enter your friend's email"
                            :append-icon="iconPlusCircle"
                            :error="errorFriendLookup"
                            :error-messages="errorFriendLookup"
                            @click:append="addFriend"
                            @keydown="addFriend"
                            solo
                        ></v-text-field>
                        <template v-if="selectedFriends.length > 0">
                            <p class="body-3">Selected users:</p>
                            <ItemList class="mb-8" :items="selectedFriends" :button-action="removeFriend" />
                        </template>
                        <template v-if="associatedFriends.length > 0">
                            <p class="body-3">You can select user from your friends:</p>
                            <ItemList :items="displayedAssociatedFriends" :button-action="selectFriend" />
                        </template>
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
                    <v-card-text class="session-user-selector__popup-content session-user-selector__popup-content--unauthorized pb-4">
                        <div class="session-user-selector__popup-header mb-10">
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
                                href="/login/"
                                >Login
                            </v-btn>
                            <v-btn class="mb-4 pl-6 pr-6" href="/signup/" block outlined>Create account </v-btn>
                        </div>
                    </v-card-text>
                </div>
            </v-card>
        </v-dialog>

    </div>
</template>

<script src="./SessionUserSelector.js" />
<style src="./SessionUserSelector.css" />