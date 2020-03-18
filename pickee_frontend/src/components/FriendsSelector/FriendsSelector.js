import { mdiPlusCircle, mdiPlus, mdiClose } from '@mdi/js';

export default {
    name: "FriendSelector",
    data: () => ({
        iconPlusCircle: mdiPlusCircle,
        iconPlus: mdiPlus,
        iconClose: mdiClose,
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