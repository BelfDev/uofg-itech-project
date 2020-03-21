<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <div class="profile-page-blocks">
                        <ActorGrid :addMethod="addActor" :removeMethod="removeActor" :items="actorItems" />
                        <MovieGrid :addMethod="addMovie" :removeMethod="removeMovie" class="mt-12" :items="movieItems" />
                        <GenrePreferences :changeEvent="updateGenres" />
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
    import ActorGrid from "@/components/ActorGrid/ActorGrid.vue";
    import MovieGrid from "@/components/MovieGrid/MovieGrid.vue";
    import GenrePreferences from "@/components/GenrePreferences/GenrePreferences.vue";
    import { mdiMinusCircle } from '@mdi/js';

    export default {
        name: "Preferences",
        data: function() {
            return {
                actorItems: [],
                movieItems: []
            };
        },
        components: { 
            PageHeader, 
            ProfileNavDrawer, 
            ActorGrid, 
            MovieGrid, 
            GenrePreferences 
        },
        methods: {
            addActor: async function (name) {
                if (name != null) {
                    const response = await http.addFavoriteActor(name);
                    this.actorItems.push({ "text": response.text, "image": response.image, "icon": mdiMinusCircle });
                }
            },
            removeActor: async function (targetItem) {
                console.log('removeActor');
                const response = http.removeFavoriteActor(name);
                console.log(response);

                // if(response.status === 200) {
                    const targetItemIndex = this.actorItems.findIndex(sourceItem => sourceItem.text === targetItem.text);
                    this.actorItems.splice(targetItemIndex, 1);
                // }
            },
            addMovie: async function (name) {
                if (name != null) {
                    const response = await http.addFavoriteMovie(name);
                    this.movieItems.push({ "text": response.text, "picture": response.picture, "icon": mdiMinusCircle });
                }
            },
            removeMovie: async function (targetItem) {
                console.log('removeMovie');
                const response = http.removeFavoriteMovie(name);
                console.log(response);

                // if(response.status === 200) {
                    const targetItemIndex = this.movieItems.findIndex(sourceItem => sourceItem.text === targetItem.text);
                    this.movieItems.splice(targetItemIndex, 1);
                // }
            },
            updateGenres: async function(data) {
                console.log('updateGenres')
                const response = http.updateFavoriteGenres(data);
                console.log(response);
            }
        },
        mounted: async function() {
            const actorsResponse = await http.getFavoriteActors();
            this.actorItems = actorsResponse.map(item => ({
                image: item.image,
                text: item.text,
                icon: mdiMinusCircle
            }));

            const moviesResponse = await http.getFavoriteMovies();
            this.movieItems = moviesResponse.map(item => ({
                picture: item.picture,
                text: item.text,
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


