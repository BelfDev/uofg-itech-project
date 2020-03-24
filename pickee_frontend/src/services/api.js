import {
    postJsonRequest,
    putJsonRequest,
    patchJsonRequest,
    deleteJsonRequest,
    getJsonRequest
} from "./http";

/**
 * HELPER METHODS
 */

const _addFavoriteGenres = async function(userID, favGenres, genreIDs) {
    genreIDs.forEach(async id => {
        if(!favGenres.find(fg => fg.genre === id)) {
            const params = {
                user: userID,
                genre: id
            }
            await postJsonRequest(`/users/${userID}/favorite-genres/`, params)
        }
    });
};

const _deleteFavoriteGenres = async function(userID, favGenres, genreIDs) {
    favGenres.forEach(async el => {
        if(genreIDs.indexOf(el.genre) === -1) {
            await deleteJsonRequest(`/users/${userID}/favorite-genres/${el.id}`)
        }
    });
};




export default {
    async createSession(userIDs) {
        const params = {
            users: userIDs
        }
        return await postJsonRequest(`/sessions/`, params);
    },

    async getGenres() {
        return await getJsonRequest(`/genres/`);
    },

    async getFavoriteGenres(userID) {
        return await getJsonRequest(`/users/${userID}/favorite-genres/`)
    },

    async updateFavoriteGenres(userID, genreIDs, isAdded) {
        const favGenres = await getJsonRequest(`/users/${userID}/favorite-genres/`);
        
        if (isAdded) {
            _addFavoriteGenres(userID, favGenres, genreIDs);
        }
        else {
            _deleteFavoriteGenres(userID, favGenres, genreIDs)
        }
    },

    async getFriend(email) {
        return await getJsonRequest(`/users/?email=${email}`);
    },

    async removeFriend(userID, friendsIDs) {
        const params = {
            associated_users: friendsIDs
        }
        return await patchJsonRequest(`/users/${userID}/`, params);
    },

    async getFriends(userID) {
        const userResponse = await getJsonRequest(`/users/${userID}/`);
        const usersData = [];
        const assocUsers = userResponse.associated_users;
        for (let i = 0; i < assocUsers.length; i++) {
            const assocUserResponse = await getJsonRequest(`/users/${assocUsers[i]}/`);
            usersData.push(assocUserResponse);
        }
        return usersData;
    },

    async getFavoriteActors(userID) {
        return await getJsonRequest(`/users/${userID}/favorite-actors/`);
    },

    async addFavoriteActors(userID, actors) {
        const favActors = [];
        for(let i = 0; i < actors.length; i++) {
            const params = actors[i].actor;
            const existingActorResponse = await getJsonRequest(`/actors/${params.id}`);
            if(!existingActorResponse.id) {
                const actorResponse = await postJsonRequest('/actors/', params);
                favActors.push({ user: userID, actor: actorResponse.id });
            } else {
                favActors.push({ user: userID, actor: params.id });
            }
        }

        return await postJsonRequest(`/users/${userID}/favorite-actors/`, favActors);
    },

    async getActor(actorID) {
        return await getJsonRequest(`/actors/${actorID}`);
    },

    async searchActor(name) {
        return await getJsonRequest(`/search/actors/?name=${name}`);
    },

    async removeFavoriteActors(userID, actorID) {
        return await deleteJsonRequest(`/users/${userID}/favorite-actors/${actorID}/`);
    },

    async getFavoriteMovies(userID) {
        return await getJsonRequest(`/users/${userID}/favorite-movies/`);
    },

    async addFavoriteMovies(userID, movies) {
        const favMovies = [];
        for(let i = 0; i < movies.length; i++) {
            const params = movies[i].movie;
            const existingMovieResponse = await getJsonRequest(`/movies/${params.id}`);
            if(!existingMovieResponse.id) {
                const movieResponse = await postJsonRequest('/movies/', params);
                favMovies.push({ user: userID, movie: movieResponse.id });
            } else {
                favMovies.push({ user: userID, movie: params.id });
            }
        }

        return await postJsonRequest(`/users/${userID}/favorite-movies/`, favMovies);
    },

    async removeFavoriteMovies(userID, movieID) {
        return await deleteJsonRequest(`/users/${userID}/favorite-movies/${movieID}/`);
    },

    async searchMovie(name) {
        return await getJsonRequest(`/search/movies/?name=${name}`);
    },

    async getMovie(movieID) {
        return await getJsonRequest(`/movies/${movieID}`);
    },

    async updateUserProfile(userID, params) {
        return await patchJsonRequest(`/users/${userID}/`, params);
    },

    async getRecommendation(preferences, sessionID, offset) {
        const params = {
            "runtime": preferences.runtime,
            "genre_ids": preferences.genre_ids,
            "user_ids": preferences.user_ids,
            "offset": offset
        };

        if (sessionID) params.session_id = sessionID;

        return await postJsonRequest(`/recommendations/generate`, params);
    },

    async setRecommendationUserChoice(recommendationID, sessionID, movieID, userChoice) {
        const params = {
            user_choice: userChoice,
            movie: movieID,
            session: sessionID
        };

        return await putJsonRequest(`/recommendations/${recommendationID}/`, params);
    },

    async getProviderList(name) {
        return await getJsonRequest(`/providers/?movie_name=${name}`)
    }
};
