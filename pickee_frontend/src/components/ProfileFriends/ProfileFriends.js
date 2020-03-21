import ItemList from "@/components/ItemList/ItemList.vue";

export default {
    name: "ProfileFriends",
    components: {
        ItemList
    },
    props: ['items', 'removeFriend'],
};
