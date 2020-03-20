import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiPlusCircle, mdiPlus, mdiClose, mdiMinusCircle, mdiAccount } from '@mdi/js';

export default {
    name: "FriendsSelector",
    components: {
        ItemList
    },
    methods: {
        removeFriend: function(name) {
            console.log('removeFriend', name)
        }
    },
    data: () => ({
        // TODO: get from API
        // user: false,
        user: { id: 1 },
        items: [
            {
                image: "https://cdn.vuetifyjs.com/images/john.jpg",
                text: "Johnny Depp",
                icon: mdiMinusCircle
            },
            {
                image: "https://cdn.vuetifyjs.com/images/john.jpg",
                text: "Brad Pitt",
                icon: mdiMinusCircle
            },
            {
                image: "https://cdn.vuetifyjs.com/images/john.jpg",
                text: "Matt Damon",
                icon: mdiMinusCircle
            }
        ],
        iconUser: mdiAccount,
        iconPlusCircle: mdiPlusCircle,
        iconPlus: mdiPlus,
        iconClose: mdiClose,
        dialog: false,
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