import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiThumbDown, mdiThumbUp, mdiBookmark } from '@mdi/js';

export default {
    name: "ProfileFriends",
    components: {
        ItemList
    },

    data: () => ({
        items: [
            {
                image: "https://movieposters2.com/images/709306-b.jpg",
                text: "Contagion",
                icon: mdiThumbDown,
                color: 'red'
            },
            {
                image: "https://cdn10.bigcommerce.com/s-o6vy9cv/products/136032/images/132304/506991__02213.1519287955.500.500.jpg?c=2",
                text: "World War Z",
                icon: mdiBookmark,
                color: 'primary'
            },
            {
                image: "https://upload.wikimedia.org/wikipedia/en/e/e4/28_days_later.jpg",
                text: "28 Days Later",
                icon: mdiThumbUp,
                color: 'green'
            }
        ]
    })
};
