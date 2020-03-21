<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <ProfileHeader :user="data.user" />
                    <div class="profile-page-blocks">
                        <ProfilePersonalDetails :updatePersonalDetails="updatePersonalDetails" :user="data.user" class="mt-12" />
                        <ProfileFriends :removeFriend="removeFriend" :items="friendsItems" class="mt-12" />
                    </div>
                </v-content>
            </main>
        </div>
    </v-app>
</template>

<script>
    import http from "@/services/http";
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
                friendsItems: []
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
            removeFriend: function(targetItem) {
                console.log('removeFriend', targetItem.text);
                const response = http.removeFriend();
                console.log(response);

                // if(response.status === 200) {
                    const targetItemIndex = this.friendsItems.findIndex(sourceItem => sourceItem.text === targetItem.text);
                    this.friendsItems.splice(targetItemIndex, 1);
                // }
            },
            updatePersonalDetails: function(data) {
                console.log('updatePersonalDetails', data);
                const response = http.updateUserProfile(data);
                console.log(response);
            }
        },
        mounted: async function() {
            const friendsResponse = await http.getFriends();
            this.friendsItems = friendsResponse.map(friend => ({
                image: friend.picture,
                text: `${friend.first_name} ${friend.last_name}`,
                icon: mdiMinusCircle
            }));
        },
        beforeMount() {
            const appElement = document.getElementsByTagName('app')[0];
            const data = appElement.getAttribute('data');
            if (data) {
                this.data = JSON.parse(data);
            }
        }
    };
</script>
