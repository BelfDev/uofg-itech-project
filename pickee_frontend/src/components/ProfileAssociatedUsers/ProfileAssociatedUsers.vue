<template>
    <div class="content-card-box">
        <h3 class="content-card-box__header">Friends</h3>
        <v-card dark>
            <v-card-text>
                <p v-if="ascUsersItems.length === 0">We don't know your friends yet. Add some!</p>
                <ItemList :items="ascUsersItems" :button-action="removeAscUser" />

                <v-dialog v-model="dialog" :width="user.id ? '100rem' : '64rem'" @click:outside="saveAscUsers">
                    <template v-slot:activator="{ on }">
                        <div class="mt-6 text-right" v-on="on">
                            <v-btn color="primary">Manage friends</v-btn>
                        </div>
                    </template>

                    <v-card light>
                        <div class="px-8 py-6 px-p-4 py-p-3">
                            <v-icon
                                class="dialog-close"
                                large
                                color="black"
                                @click="dialog = false; saveAscUsers()"
                                >{{ iconClose }}</v-icon>
                            <v-card-text class="associated-user-selector__popup-content pb-4">
                                <div class="associated-user-selector__popup-header mb-8">
                                    <v-avatar size="10rem">
                                        <img :src="user.picture" :alt="user.name" v-if="user.picture" />
                                        <v-icon color="secondary" v-else>{{ iconUser }}</v-icon>
                                    </v-avatar>
                                    <p>Hey {{ user.name }}, <strong>add friends</strong> to your movie session by typing their user ids in the list below</p>
                                </div>
                                <v-text-field
                                    dark
                                    v-model="userEmail"
                                    label="Enter your friend's email"
                                    :append-icon="iconPlusCircle"
                                    :error="errorUserLookup.length > 0"
                                    :error-messages="errorUserLookup"
                                    @click:append="addAscUser"
                                    @keydown="addAscUser"
                                    solo
                                ></v-text-field>
                                <ItemList 
                                    v-if="ascUsersItems.length > 0" 
                                    class="mb-8" 
                                    :items="ascUsersItems" 
                                    :button-action="removeAscUser" 
                                />
                            </v-card-text>

                            <v-card-actions class="dialog-actions text-right">
                                <button class="dialog-actions__button" @click="dialog = false; saveAscUsers()">Done</button>
                            </v-card-actions>
                        </div>
                    </v-card>
                </v-dialog>
            </v-card-text>
        </v-card>
    </div>
</template>

<script src="./ProfileAssociatedUsers.js" />
<style src="./ProfileAssociatedUsers.css" />
