import ItemList from "@/components/ItemList/ItemList.vue";

export default {
    name: "ProfileAssociatedUsers",
    components: {
        ItemList
    },
    props: ['items', 'removeAscUser'],
};
