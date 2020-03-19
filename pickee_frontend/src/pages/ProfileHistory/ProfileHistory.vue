<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <PageHeader />
        </div>
    </v-app>
</template>

<script>
    import PageHeader from "@/components/PageHeader/PageHeader.vue";
    import ProfileNavDrawer from "@/components/ProfileNavDrawer/ProfileNavDrawer.vue";

    export default {
        name: "ProfileHistory",
        data: function() {
            return {};
        },
        components: { PageHeader, ProfileNavDrawer }
    };
</script>
