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
    }
};
