import ItemsSearch from "@/components/ItemsSearch/ItemsSearch.vue";
import { mdiClose } from "@mdi/js";

export default {
    name: "AddItemDialog",
    props: [
        "addButtonText",
        "entries",
        "items",
        "addMethod",
        "removeMethod",
        "searchMethod",
        "saveMethod",
        "searchLoading",
    ],
    components: {
        ItemsSearch
    },
    data: () => ({
        dialog: false,
        iconClose: mdiClose
    })
};
