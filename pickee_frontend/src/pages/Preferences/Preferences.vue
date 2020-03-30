<template>
    <v-app>
        <div class="profile-page">
            <ProfileNavDrawer />
            <main class="profile-page-main">
                <PageHeader />
                <v-content class="profile-page-content">
                    <div class="profile-page-blocks">
                        <PreferencesGrid 
                            addButtonText="Manage actors"
                            boxTitle="Favorite Actors"
                            type="actors"
                            :addMethod="addActor" 
                            :removeMethod="removeActor" 
                            :searchMethod="searchActor"
                            :saveMethod="saveActors"
                            :entries="actorLookup" 
                            :items="actorItems"
                            :searchLoading="isActorLookupLoading"
                        />
                        <PreferencesGrid 
                            class="mt-12" 
                            addButtonText="Manage movies"
                            boxTitle="Favorite Movies"
                            type="movies"
                            :addMethod="addMovie" 
                            :removeMethod="removeMovie" 
                            :searchMethod="searchMovie"
                            :saveMethod="saveMovies"
                            :entries="movieLookup" 
                            :items="movieItems" 
                            :searchLoading="isMovieLookupLoading"
                        />
                        <GenrePreferences 
                            v-if="selectedGenres"
                            :items="genreItems" 
                            :selected="selectedGenres" 
                            :changeEvent="updateGenres" 
                            @input="(newSelectedGenres) => { selectedGenres = newSelectedGenres }"
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
    import PreferencesGrid from "@/components/PreferencesGrid/PreferencesGrid.vue";
    import GenrePreferences from "@/components/GenrePreferences/GenrePreferences.vue";
    import { mdiMinusCircle } from '@mdi/js';

    export default {
        name: "Preferences",
        data: function() {
            return {
                actorLookup: null,
                movieLookup: null,
                actorItems: [],
                newFavoriteActors: [],
                removedFavoriteActors: [],
                movieItems: [],
                newFavoriteMovies: [],
                removedFavoriteMovies: [],
                genreItems: [],
                selectedGenres: null,
                userID: null,
                isActorLookupLoading: false,
                isMovieLookupLoading: false
            };
        },
        components: { 
            PageHeader, 
            ProfileNavDrawer, 
            PreferencesGrid, 
            GenrePreferences 
        },
        methods: {
            addActor: async function (actor) {
                this.newFavoriteActors.push({ user: this.userID, actor })
                this.actorItems.push({ 
                    id: actor.id,
                    text: actor.name, 
                    image: actor.image_url, 
                    icon: mdiMinusCircle 
                });
            },

            removeActor: async function (actor) {
                const targetItemIndex = this.actorItems.findIndex(sourceItem => sourceItem.text === actor.text);
                this.actorItems.splice(targetItemIndex, 1);
                this.removedFavoriteActors.push(actor.refID)
            },
            
            searchActor: async function (name) {
                this.isActorLookupLoading = true;
                const response = await api.searchActor(name);
                this.actorLookup = response.results || [];
                this.isActorLookupLoading = false;
            },
            
            saveActors: async function() {
                // Add new actors
                if (this.newFavoriteActors.length > 0) {
                    const response = await api.addFavoriteActors(this.userID, this.newFavoriteActors);
                    response.forEach(res => {
                        const t = this.actorItems.find(v => v.id === res.actor);
                        t.refID = res.id;
                    });
                    this.newFavoriteActors = [];
                }

                // Remove selected actors
                if (this.removedFavoriteActors.length > 0) {
                    for (let i = 0; i < this.removedFavoriteActors.length; i++) {
                        await api.removeFavoriteActors(this.userID, this.removedFavoriteActors[i]);
                    }
                    this.removedFavoriteActors = []
                }
            },

            addMovie: async function (movie) {
                this.newFavoriteMovies.push({ user: this.userID, movie })
                this.movieItems.push({ 
                    id: movie.id,
                    text: movie.name, 
                    picture: movie.image_url, 
                    icon: mdiMinusCircle 
                });
            },
            
            removeMovie: async function (movie) {
                const targetItemIndex = this.movieItems.findIndex(sourceItem => sourceItem.text === movie.text);
                this.movieItems.splice(targetItemIndex, 1);
                this.removedFavoriteMovies.push(movie.refID);
            },
            
            searchMovie: async function(name) {
                this.isMovieLookupLoading = true;
                const response = await api.searchMovie(name);
                this.movieLookup = response.results || [];
                this.isMovieLookupLoading = false;
            },
            
            saveMovies: async function() {
                // Add new movies
                if (this.newFavoriteMovies.length > 0) {
                    const response = await api.addFavoriteMovies(this.userID, this.newFavoriteMovies);
                    response.forEach(res => {
                        const t = this.movieItems.find(v => v.id === res.movie);
                        t.refID = res.id;
                    });
                    this.newFavoriteMovies = [];
                }

                // Remove selected movies
                if (this.removedFavoriteMovies.length > 0) {
                    for (let i = 0; i < this.removedFavoriteMovies.length; i++) {
                        await api.removeFavoriteMovies(this.userID, this.removedFavoriteMovies[i]);
                    }
                    this.removedFavoriteMovies = [];
                }
            },

            updateGenres: async function(values) {
                const genreIDs = values.map(v => {
                    const matchIndex = this.genreItems.findIndex(k => k.text === v);
                    return this.genreItems[matchIndex].value;
                });
                const isAdded = values.length > this.selectedGenres.length;
                api.updateFavoriteGenres(this.userID, genreIDs, isAdded);
            },

            _fetchActors: async function() {
                const actorsResponse = await api.getFavoriteActors(this.userID);
                const actors = [];
                for (let i = 0; i < actorsResponse.length; i++) {
                    const actorData = await api.getActor(actorsResponse[i].actor);
                    actors.push({
                        id: actorData.id,
                        refID: actorsResponse[i].id,
                        image: actorData.image_url,
                        text: actorData.name,
                        icon: mdiMinusCircle
                    })
                }
                this.actorItems = actors;
            },

            _fetchMovies: async function() {
                const moviesResponse = await api.getFavoriteMovies(this.userID);
                const movies = [];
                for (let i = 0; i < moviesResponse.length; i++) {
                    const movieData = await api.getMovie(moviesResponse[i].movie);
                    movies.push({
                        id: movieData.id,
                        refID: moviesResponse[i].id,
                        picture: movieData.image_url,
                        text: movieData.name,
                        icon: mdiMinusCircle
                    })
                }
                this.movieItems = movies;
            },

            _fetchGenres: async function() {
                const response = await api.getGenres();
                this.genreItems = response.map(item => ({
                    text: item.name,
                    value: item.id
                }));
                const genreResponse = await api.getFavoriteGenres(this.userID);
                this.selectedGenres = genreResponse.map(favGenre => {
                    const genre = this.genreItems.find(k => k.value === favGenre.genre);
                    return genre.text
                })
            }
        },
        mounted: async function() {
            this._fetchActors();
            this._fetchMovies();
            this._fetchGenres();
        },
        beforeMount() {
            const appElement = document.getElementsByTagName('app')[0];
            let user = appElement.getAttribute('user');
            if (user) {
                user = JSON.parse(user);
                this.userID = user.id;
            }
        }
    };
</script>


