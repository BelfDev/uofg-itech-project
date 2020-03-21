import axios from "axios";

const APIBase = "/api";

export default {
    async getGenres() {
        const response = await axios.get(`${APIBase}/genres/`);

        return response;
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

    async updateUserProfile(data) {
        console.log(data);

        // send request

        return await Promise.resolve(1);
    }
};
