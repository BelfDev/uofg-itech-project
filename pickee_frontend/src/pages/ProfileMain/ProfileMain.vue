<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <ProfileHeader />
                    <div class="profile-page-blocks">
                        <ProfilePersonalDetails class="mt-12" />
                        <ProfileFriends class="mt-12" />
                    </div>
                </v-content>
            </main>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from "@/components/PageHeader/PageHeader.vue";
    import ProfileNavDrawer from "@/components/ProfileNavDrawer/ProfileNavDrawer.vue";
    import ProfileHeader from "@/components/ProfileHeader/ProfileHeader.vue";
    import ProfilePersonalDetails from "@/components/ProfilePersonalDetails/ProfilePersonalDetails.vue";
    import ProfileFriends from "@/components/ProfileFriends/ProfileFriends.vue";

    export default {
        name: "ProfileMain",
        data: function() {
            return {};
        },
        components: { 
            PageHeader, 
            ProfileNavDrawer, 
            ProfileHeader, 
            ProfilePersonalDetails, 
            ProfileFriends
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
