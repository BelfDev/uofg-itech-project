import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiThumbDown, mdiThumbUp, mdiBookmark, mdiClose } from '@mdi/js';
import http from "@/services/http";

export default {
    name: "RecommendationDescr",
    props: ['recommendation', 'newRecEvent'],
    components: {
        ItemList
    },
    methods: {
        openProvider: function(link) {
            window.open(link);
            this.dialog = false;
        },
        getProviderList: async function() {
            console.log(http);
            const response = await http.getProviderList();
            console.log(response);
            this.providerList = response;
        }
    },
    computed: {
        recMovieReleaseDate: function() {
            const date = new Date(this.recommendation.release_date);
            const day = date.getDate();
            const month = date.getMonth();
            const year = date.getFullYear();
            return `${day}.${month}.${year}`;
        }
    },
    data: () => ({
        iconFavorites: mdiBookmark,
        iconThumbDown: mdiThumbDown,
        iconThumbUp: mdiThumbUp,
        iconClose: mdiClose,
        ratingValue: 74,
        dialog: false,
        providerList: [],
    })
}