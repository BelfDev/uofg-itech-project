<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <ProfileHeader :user="user" />
                    <div class="profile-page-blocks">
                        <ProfilePersonalDetails 
                            class="mt-12"
                            :updatePersonalDetails="updatePersonalDetails" 
                            :user="user" 
                        />
                        <ProfileAssociatedUsers 
                            class="mt-12"
                            :user="user"
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
    import ProfileAssociatedUsers from "@/components/ProfileAssociatedUsers/ProfileAssociatedUsers.vue";

    export default {
        name: "Profile",
        data: function() {
            return {
                user: null,
                userID: null,
            };
        },
        components: { 
            PageHeader, 
            ProfileNavDrawer, 
            ProfileHeader, 
            ProfilePersonalDetails, 
            ProfileAssociatedUsers
        },
        methods: {
            updatePersonalDetails: async function(name, value) {
                const params = {};
                params[name] = value;
                await api.updateUserProfile(this.userID, params);
            }
        },
        beforeMount() {
            const appElement = document.getElementsByTagName('app')[0];
            let user = appElement.getAttribute('user');
            if (user) {
                this.user = JSON.parse(user);
                this.userID = this.user.id;
            }
        }
    };
</script>
