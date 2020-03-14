<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                <ProfileHeader />
                </v-content>
            </main>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from "@/components/PageHeader/PageHeader.vue";
    import ProfileNavDrawer from "@/components/ProfileNavDrawer/ProfileNavDrawer.vue";
    import ProfileHeader from "@/components/ProfileHeader/ProfileHeader.vue";

    export default {
        name: "ProfileMain",
        data: function() {
            return {};
        },
        components: { PageHeader, ProfileNavDrawer, ProfileHeader }
    };
</script>
