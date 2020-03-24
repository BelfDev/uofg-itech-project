<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <ProfileHeader :user="data.user" />
                    <div class="profile-page-blocks">
                        <ProfilePersonalDetails 
                            class="mt-12"
                            :updatePersonalDetails="updatePersonalDetails" 
                            :user="data.user" 
                        />
                        <ProfileFriends 
                            class="mt-12"
                            :removeFriend="removeFriend" 
                            :items="friendsItems" 
                        />
                    </div>
                </v-content>
            </main>
        </div>
    </v-app>
</template>

<script>
    import api from "@/services/api";
    import PageHeader from "@/components/PageHeader/PageHeader.vue";
    import ProfileNavDrawer from "@/components/ProfileNavDrawer/ProfileNavDrawer.vue";
    import ProfileHeader from "@/components/ProfileHeader/ProfileHeader.vue";
    import ProfilePersonalDetails from "@/components/ProfilePersonalDetails/ProfilePersonalDetails.vue";
    import ProfileFriends from "@/components/ProfileFriends/ProfileFriends.vue";
    import { mdiMinusCircle } from "@mdi/js";

    export default {
        name: "Profile",
        data: function() {
            return {
                friendsItems: [],
                friendsIDs: [],
                userID: null,
            };
        },
        components: { 
            PageHeader, 
            ProfileNavDrawer, 
            ProfileHeader, 
            ProfilePersonalDetails, 
            ProfileFriends
        },
        methods: {
            removeFriend: async function(friend) {
                const targetItemIndex = this.friendsItems.findIndex(sourceItem => sourceItem.text === friend.text);
                this.friendsItems.splice(targetItemIndex, 1);
                this.friendsIDs.splice(targetItemIndex, 1);

                await api.removeFriend(this.userID, this.friendsIDs);
            },
            updatePersonalDetails: async function(name, value) {
                const params = {};
                params[name] = value;
                await api.updateUserProfile(this.userID, params);
            }
        },
        mounted: async function() {
            const friendsResponse = await api.getFriends(this.userID);
            this.friendsItems = friendsResponse.map(friend => {
                this.friendsIDs.push(friend.id);
                return {
                    id: friend.id,
                    image: friend.picture,
                    text: `${friend.first_name} ${friend.last_name}`,
                    icon: mdiMinusCircle
                }
            });
            console.log(this.friendsIDs);
        },
        beforeMount() {
            const appElement = document.getElementsByTagName('app')[0];
            let data = appElement.getAttribute('data');
            if (data) {
                this.data = JSON.parse(data);
                this.userID = this.data.user.id;
            }
        }
    };
</script>
