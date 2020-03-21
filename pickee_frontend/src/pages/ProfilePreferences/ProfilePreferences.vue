<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <div class="profile-page-blocks">
                        <ActorGrid :items="actorItems" />
                        <MovieGrid :items="movieItems" />
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
    import ActorGrid from "@/components/ActorGrid/ActorGrid.vue";
    import MovieGrid from "@/components/MovieGrid/MovieGrid.vue";
    import ChipBox from "@/components/ChipBox/ChipBox.vue";
    import { mdiMinusCircle } from '@mdi/js';

    export default {
        name: "ProfilePreferences",
        data: function() {
            return {
                actorItems: [
                    {
                        text: "Johny Depp",
                        image: "https://cdn.vuetifyjs.com/images/john.jpg",
                        icon: mdiMinusCircle
                    }, {
                        text: "Brad Pitt",
                        image: "https://cdn.vuetifyjs.com/images/john.jpg",
                        icon: mdiMinusCircle
                    }, {
                        text: "Leonardo Di Caprio",
                        image: "https://cdn.vuetifyjs.com/images/john.jpg",
                        icon: mdiMinusCircle
                    }, {
                        text: "Nicholas Cage",
                        image: "https://cdn.vuetifyjs.com/images/john.jpg",
                        icon: mdiMinusCircle
                    }, {
                        text: "Sylvester Stallone",
                        image: "https://cdn.vuetifyjs.com/images/john.jpg",
                        icon: mdiMinusCircle
                    }
                ],
                movieItems: [
                    {
                        text: "It's a Wonderful Life",
                        picture: "https://image.tmdb.org/t/p/w500/bSqt9rhDZx1Q7UZ86dBPKdNomp2.jpg",
                        icon: mdiMinusCircle
                    }, {
                        text: "Coco",
                        picture: "https://image.tmdb.org/t/p/w500/eKi8dIrr8voobbaGzDpe8w0PVbC.jpg",
                        icon: mdiMinusCircle
                    }, {
                        text: "Harry Potter and the Deathly Hallows: Part 2",
                        picture: "https://image.tmdb.org/t/p/w500/fTplI1NCSuEDP4ITLcTps739fcC.jpg",
                        icon: mdiMinusCircle
                    }
                ]
            };
        },
        components: { PageHeader, ProfileNavDrawer, ActorGrid, MovieGrid, ChipBox }
    };
</script>


