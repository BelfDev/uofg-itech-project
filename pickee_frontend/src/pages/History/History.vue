<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <div class="profile-page-blocks">
                        <ProfileHistoryList :historyItems="historyItems" />
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
    import { mdiThumbDown, mdiThumbUp, mdiBookmark } from '@mdi/js';

    const choiceIconMap = {
        "REJECTED": {
            icon: mdiThumbDown,
            color: 'red'
        },
        "ACCEPTED": {
            icon: mdiThumbUp,
            color: 'green'
        },
        "BOOKMARKED": {
            icon: mdiBookmark,
            color: 'primary'
        }
    }

    export default {
        name: "History",
        data: function() {
            return {
                historyItems: []
            };
        },
        components: { PageHeader, ProfileNavDrawer, ProfileHistoryList },
        beforeMount() {
            const appElement = document.getElementsByTagName('app')[0];
            const data = appElement.getAttribute('data');
            if (data) {
                this.data = JSON.parse(data);
                this.historyItems = this.data.results.map(item => ({
                    image: item.movie.image_url,
                    text: item.movie.name,
                    icon: choiceIconMap[item.user_choice].icon,
                    color: choiceIconMap[item.user_choice].color
                }));
            }
        }
    };
</script>

