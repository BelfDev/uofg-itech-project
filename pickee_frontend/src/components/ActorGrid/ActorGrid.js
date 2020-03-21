import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiMagnify, mdiClose } from '@mdi/js';

export default {
    name: "ActorGrid",
    props: ['items'],
    data: () => ({
        dialog: false,
        iconSearch: mdiMagnify,
        iconClose: mdiClose,
    }),
    methods: {
        removeItem: function(name) {
            console.log('removeItem', name)
        }
    },
    components: {
        ItemList
    }
}