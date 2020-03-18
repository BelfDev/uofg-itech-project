import { mdiPlus } from '@mdi/js';

export default {
    name: "FriendSelector",
    data: () => ({
        iconPlus: mdiPlus,
        selectedFriends: [
            {
                id: 1,
                name: "John",
                avatar: "https://cdn.vuetifyjs.com/images/john.jpg"
            },
            {
                id: 2,
                name: "John",
                avatar: "https://cdn.vuetifyjs.com/images/john.jpg"
            },
            {
                id: 3,
                name: "John",
                avatar: "https://cdn.vuetifyjs.com/images/john.jpg"
            },
            {
                id: 4,
                name: "John",
                avatar: "https://cdn.vuetifyjs.com/images/john.jpg"
            }
        ]
    })
}