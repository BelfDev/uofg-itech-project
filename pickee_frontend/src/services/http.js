import axios from "axios";

const APIBase = "/api";

export default {
    async getGenres() {
        const response = await axios.get(`${APIBase}/genres/`);

        return response;
    },

    async updateFavoriteGenres(genres) {
        // send request

        console.log(genres);
        return await Promise.resolve(1);
    },

    async getFriend() {
        // await axios.get(`${APIBase}/genres/${email}`);
        return await {
            id: Math.floor(Math.random() * 100) + 1, // temp
            email: "anton@qwe.qwe",
            first_name: "Anton",
            last_name: "",
            picture:
                "http://127.0.0.1:8000/media/profile_images/abcasd_U6uAG94.png",
            gender: null,
            age: null,
            associated_users: []
        };
    },

    async removeFriend() {
        // send request

        return await Promise.resolve(1);
    },

    async getFriends() {
        return await [{
            id: 1,
            email: "anton@qwe.qwe",
            first_name: "Anton",
            last_name: "",
            picture:
                "http://127.0.0.1:8000/media/profile_images/abcasd_U6uAG94.png"
        }, {
            id: 2,
            email: "pedro@qwe.qwe",
            first_name: "Pedro",
            last_name: "",
            picture:
                "http://127.0.0.1:8000/media/profile_images/abcasd_U6uAG94.png"
        }, {
            id: 3,
            email: "Rhys@qwe.qwe",
            first_name: "Rhys",
            last_name: "",
            picture:
                "http://127.0.0.1:8000/media/profile_images/abcasd_U6uAG94.png"
        }]
    },

    async getFavoriteActors() {
        return await [
            {
                text: "Johny Depp",
                image: "https://cdn.vuetifyjs.com/images/john.jpg",
            }, {
                text: "Brad Pitt",
                image: "https://cdn.vuetifyjs.com/images/john.jpg",
            }, {
                text: "Leonardo Di Caprio",
                image: "https://cdn.vuetifyjs.com/images/john.jpg",
            }, {
                text: "Nicholas Cage",
                image: "https://cdn.vuetifyjs.com/images/john.jpg",
            }
        ]
    },

    async addFavoriteActor() {
        return await {
            text: "Sylvester Stallone",
            image: "https://cdn.vuetifyjs.com/images/john.jpg",
        }
    },

    async removeFavoriteActor() {
        // send request

        return await Promise.resolve(1);
    },

    async getFavoriteMovies() {
        return await [
            {
                text: "It's a Wonderful Life",
                picture: "https://image.tmdb.org/t/p/w500/bSqt9rhDZx1Q7UZ86dBPKdNomp2.jpg",
            }, {
                text: "Coco",
                picture: "https://image.tmdb.org/t/p/w500/eKi8dIrr8voobbaGzDpe8w0PVbC.jpg",
            }, {
                text: "Harry Potter and the Deathly Hallows: Part 2",
                picture: "https://image.tmdb.org/t/p/w500/fTplI1NCSuEDP4ITLcTps739fcC.jpg"
            }
        ]
    },

    async addFavoriteMovie() {
        return await {
            text: "Gladiator",
            picture: "https://image.tmdb.org/t/p/w500/bSqt9rhDZx1Q7UZ86dBPKdNomp2.jpg",
        }
    },

    async removeFavoriteMovie() {
        // send request

        return await Promise.resolve(1);
    },

    async updateUserProfile(data) {
        console.log(data);

        // send request

        return await Promise.resolve(1);
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
    }
};
