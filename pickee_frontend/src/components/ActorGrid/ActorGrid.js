import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiMagnify, mdiClose } from '@mdi/js';

export default {
    name: "ActorGrid",
    props: ['items', 'addMethod', 'removeMethod'],
    data: () => ({
        dialog: false,
        iconSearch: mdiMagnify,
        iconClose: mdiClose,
        searchText: ''
    }),
    components: {
        ItemList
    }
}