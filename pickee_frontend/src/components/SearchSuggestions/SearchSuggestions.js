import { mdiMagnify, mdiAccount } from "@mdi/js";

export default {
    name: "SearchSuggestions",
    props: ["entries", "searchMethod", "addMethod", "searchLoading"],
    data: function() {
        return {
            searchText: "",
            iconUser: mdiAccount,
            iconSearch: mdiMagnify,
            searchInput: null
        };
    },
    methods: {
        searchEvent: function(e) {
            if (e.type === "keydown" && e.key !== "Enter")
                return false;

            this.searchMethod(this.searchText);
        },
        addEvent: function(item, index) {
            this.addMethod(item);
            this.entries.splice(index, 1);
        }
    },
    mounted: function() {
        this.searchInput = this.$refs.searchInput;
    }
};