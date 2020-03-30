import ItemList from "@/components/ItemList/ItemList.vue";
import SearchSuggestions from "@/components/SearchSuggestions/SearchSuggestions.vue";

export default {
    name: "ItemsSearch",
    props: [
        "items",
        "entries",
        "addMethod",
        "removeMethod",
        "searchMethod",
        "searchLoading"
    ],
    components: {
        ItemList,
        SearchSuggestions
    }
};
