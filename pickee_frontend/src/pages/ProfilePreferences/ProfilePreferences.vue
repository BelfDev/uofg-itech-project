<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <div class="profile-page-blocks">
                        <ImageGrid />
                        <ImageGrid />
                        <ChipBox />
                    </div>
                </v-content>
            </main>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from "@/components/PageHeader/PageHeader.vue";
    import ProfileNavDrawer from "@/components/ProfileNavDrawer/ProfileNavDrawer.vue";
    import ImageGrid from "@/components/ImageGrid/ImageGrid.vue";
    import ChipBox from "@/components/ChipBox/ChipBox.vue";

    export default {
        name: "ProfilePreferences",
        data: function() {
            return {};
        },
        components: { PageHeader, ProfileNavDrawer, ImageGrid , ChipBox }
    };
</script>


