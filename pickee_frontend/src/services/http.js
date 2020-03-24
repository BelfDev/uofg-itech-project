import axios from "axios";
import VueCookies from 'vue-cookies';

const APIBase = "/api";

const jsonRequest = async function(url, params, method) {
    const myHeaders = new Headers();
    myHeaders.append("X-CSRFToken", VueCookies.get("csrftoken"));
    myHeaders.append('Content-Type', 'application/json');

    const requestOptions = {
        method: method || 'POST',
        headers: myHeaders
    };

    if (params) requestOptions.body = JSON.stringify(params);

    let response = await fetch(url, requestOptions);

    return await response.text().then(function(text) {
        return text ? JSON.parse(text) : {}
    })
};

const addFavoriteGenres = async function(userID, favGenres, genreIDs) {
    genreIDs.forEach(async id => {
        if(!favGenres.find(fg => fg.genre === id)) {
            const params = {
                user: userID,
                genre: id
            }
            await jsonRequest(`${APIBase}/users/${userID}/favorite-genres/`, params)
        }
    });
};

const deleteFavoriteGenres = async function(userID, favGenres, genreIDs) {
    favGenres.forEach(async el => {
        if(genreIDs.indexOf(el.genre) === -1) {
            await jsonRequest(`${APIBase}/users/${userID}/favorite-genres/${el.id}`, null, 'DELETE')
        }
    });
};

export default {
    async createSession(userIDs) {
        const params = {
            users: userIDs
        }
        return await jsonRequest(`${APIBase}/sessions/`, params);
    },

    async getGenres() {
        const response = await axios.get(`${APIBase}/genres/`);

        return response;
    },

    async getFavoriteGenres(userID) {
        return await jsonRequest(`${APIBase}/users/${userID}/favorite-genres/`, null, 'GET')
    },

    async updateFavoriteGenres(userID, genreIDs, isAdded) {
        const favGenres = await jsonRequest(`${APIBase}/users/${userID}/favorite-genres/`, null, 'GET');
        
        if (isAdded) {
            addFavoriteGenres(userID, favGenres, genreIDs);
        }
        else {
            deleteFavoriteGenres(userID, favGenres, genreIDs)
        }
    },

    async getFriend(email) {
        const response = await axios.get(`${APIBase}/users/?email=${email}`);
        
        return response;
    },

    async removeFriend(userID, friendsIDs) {
        const params = {
            associated_users: friendsIDs
        }
        return await jsonRequest(`${APIBase}/users/${userID}/`, params, 'PATCH');
    },

    async getFriends(userID) {
        const userResponse = await jsonRequest(`${APIBase}/users/${userID}/`, null, 'GET');
        const usersData = [];
        const assocUsers = userResponse.associated_users;
        for (let i = 0; i < assocUsers.length; i++) {
            const assocUserResponse = await jsonRequest(`${APIBase}/users/${assocUsers[i]}/`, null, 'GET');
            usersData.push(assocUserResponse);
        }
        return usersData;
    },

    async getFavoriteActors(userID) {
        return await jsonRequest(`${APIBase}/users/${userID}/favorite-actors/`, null, 'GET');
    },

    async addFavoriteActor(userID, actors) {
        return await jsonRequest(`${APIBase}/users/${userID}/favorite-actors/`, actors);
    },

    async getActor(actorID) {
        return await jsonRequest(`${APIBase}/actors/${actorID}`, null, 'GET');
    },

    async searchActor(name) {
        return await jsonRequest(`${APIBase}/search/actors/?name=${name}`, null, 'GET');
    },

    async removeFavoriteActor(userID, actorID) {
        return await jsonRequest(`${APIBase}/users/${userID}/favorite-actors/${actorID}/`, null, 'DELETE');
    },

    async getFavoriteMovies(userID) {
        return await jsonRequest(`${APIBase}/users/${userID}/favorite-movies/`, null, 'GET');
    },

    async addFavoriteMovie(userID, movies) {
        return await jsonRequest(`${APIBase}/users/${userID}/favorite-movies/`, movies);
    },

    async removeFavoriteMovie(userID, movieID) {
        return await jsonRequest(`${APIBase}/users/${userID}/favorite-movies/${movieID}/`, null, 'DELETE');
    },

    async searchMovie(name) {
        return await jsonRequest(`${APIBase}/search/movies/?name=${name}`, null, 'GET');
    },

    async getMovie(movieID) {
        return await jsonRequest(`${APIBase}/movies/${movieID}`, null, 'GET');
    },

    async updateUserProfile(userID, params) {
        return await jsonRequest(`${APIBase}/users/${userID}/`, params, 'PATCH');
    },

    async getRecommendationHistory() {
        return await [
            {
                image: "https://movieposters2.com/images/709306-b.jpg",
                text: "Contagion",
                user_choice: "REJECTED"
            },
            {
                image: "https://cdn10.bigcommerce.com/s-o6vy9cv/products/136032/images/132304/506991__02213.1519287955.500.500.jpg?c=2",
                text: "World War Z",
                user_choice: "BOOKMARKED"
            },
            {
                image: "https://upload.wikimedia.org/wikipedia/en/e/e4/28_days_later.jpg",
                text: "28 Days Later",
                user_choice: "APPROVED"
            }
        ]
    },

    async getRecommendation(preferences, sessionID, offset) {
        const params = {
            "runtime": preferences.runtime,
            "genre_ids": preferences.genre_ids,
            "user_ids": preferences.user_ids,
            "offset": offset
        };

        if (sessionID) params.session_id = sessionID;

        return await jsonRequest(`${APIBase}/recommendations/generate`, params);
    },

    async setRecommendationUserChoice(recommendationID, sessionID, movieID, userChoice) {
        const params = {
            user_choice: userChoice,
            movie: movieID,
            session: sessionID
        };

        return await jsonRequest(`${APIBase}/recommendations/${recommendationID}/`, params, 'put');
    },

    async getProviderList(name) {
        return await jsonRequest(`${APIBase}/providers/?movie_name=${name}`, null, 'get')
    }
};
