import TimeSlider from "@/components/TimeSlider/TimeSlider.vue";
import FriendsSelector from "@/components/FriendsSelector/FriendsSelector.vue";
import { mdiPlayCircleOutline } from "@mdi/js";

export default {
    name: 'CasualPreferencesSelection',
    data: () => ({
        select: ["Action"],
        items: ["Action", "Drama", "Fantasy", "Sci-Fi"],
        iconPlay: mdiPlayCircleOutline
    }),
    components: {
        TimeSlider,
        FriendsSelector
    }
}