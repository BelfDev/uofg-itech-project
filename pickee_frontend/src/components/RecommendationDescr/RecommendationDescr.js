import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiThumbDown, mdiThumbUp, mdiBookmark, mdiClose } from '@mdi/js';

export default {
    name: "RecommendationDescr",
    props: ['recommendation', 'newRecEvent', 'acceptEvent', 'providerList', 'isLoading', 'user'],
    components: {
        ItemList
    },
    methods: {
        openProvider: function(item) {
            window.open(item.link);
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
    })
}