<template>
    <v-dialog v-model="dialog" width="100rem" @click:outside="saveMethod">
        <template v-slot:activator="{ on }">
            <div class="add-item-dialog__btn" v-on="on">
                <v-btn color="primary">{{ addButtonText }}</v-btn>
            </div>
        </template>

        <v-card light>
            <div class="px-8 py-6 px-p-4 py-p-3">
                <v-icon
                    class="dialog-close"
                    large
                    color="black"
                    @click="dialog = false; saveMethod()"
                    >{{ iconClose }}</v-icon>
                <v-card-text class="add-item-dialog__popup-content">
                    <ItemsSearch 
                        :items="items" 
                        :entries="entries"
                        :removeMethod="removeMethod"
                        :searchMethod="searchMethod"
                        :addMethod="addMethod"
                        :searchLoading="searchLoading"
                    />
                </v-card-text>
            </div>
        </v-card>
    </v-dialog>
</template>

<script src="./AddItemDialog.js" />
<style src="./AddItemDialog.css" />
