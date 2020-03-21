<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <div class="profile-page-blocks">
                        <ProfileHistoryList />
                    </div>
                </v-content>
            </main>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from "@/components/PageHeader/PageHeader.vue";
    import ProfileNavDrawer from "@/components/ProfileNavDrawer/ProfileNavDrawer.vue";
    import ProfileHistoryList from "@/components/ProfileHistoryList/ProfileHistoryList.vue";
    export default {
        name: "ProfileHistory",
        data: function() {
            return {};
        },
        components: { PageHeader, ProfileNavDrawer, ProfileHistoryList }
    };
</script>

