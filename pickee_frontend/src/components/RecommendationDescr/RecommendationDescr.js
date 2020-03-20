import ItemList from "@/components/ItemList/ItemList.vue";
import { mdiThumbDown, mdiThumbUp, mdiBookmark, mdiClose } from '@mdi/js';

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
        getProviderList: function() {
            this.providerList = [
                {
                    logo: "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/iTunesIVAGB.png?w=100&auto=compress",
                    text: "ITunes",
                    type: "Rent/Buy",
                    link: "https://itunes.apple.com/za/movie/the-dark-knight/id606743816"
                },
                {
                    logo: "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/GooglePlayIVAGB.png?w=100&auto=compress",
                    text: "Google Play",
                    type: "Rent/Buy",
                    link: "https://play.google.com/store/movies/details/The_Dark_Knight?gl=GB&hl=en&id=TQfcgaNdBCA"
                },
                {
                    logo: "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonInstantVideoIVAGB.png?w=100&auto=compress",
                    text: "Amazon Prime",
                    type: "Rent/Buy",
                    link: "https://www.amazon.co.uk/gp/product/B00I9LY2N8?creativeASIN=B00I9LY2N8&ie=UTF8&linkCode=xm2&tag=utellycom00-21"
                },
            ];
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