import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiMinusCircle } from "@mdi/js";

export default {
    name: "ProfileFriends",
    components: {
        ItemList
    },
    methods: {
        removeFriend: function(name) {
            console.log('removeFriend', name)
        }
    },
    // TODO: get from API
    data: () => ({
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
        ]
    })
};
