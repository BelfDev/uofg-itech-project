import { mdiThumbDown, mdiThumbUp, mdiBookmark } from '@mdi/js';

export default {
    name: "RecommendationDescr",
    data: () => ({
        iconFavorites: mdiBookmark,
        iconThumbDown: mdiThumbDown,
        iconThumbUp: mdiThumbUp,
        ratingValue: 74
    })
}