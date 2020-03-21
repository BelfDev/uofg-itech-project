import TimeSlider from "@/components/TimeSlider/TimeSlider.vue";
import FriendsSelector from "@/components/FriendsSelector/FriendsSelector.vue";
import http from "@/services/http";
import { mdiPlayCircleOutline } from "@mdi/js";

export default {
    name: 'CasualPreferencesSelection',
    data: function() {
        return {
            selectedGenres: [],
            items: [],
            iconPlay: mdiPlayCircleOutline,
            token: this.$cookies.get("csrftoken")
        }
    },
    props: ['user'],
    created: async function() {
        const response = await http.getGenres();
        this.items = response.data.map(item => ({
            text: item.name,
            value: item.id
        }));
    },
    components: {
        TimeSlider,
        FriendsSelector
    }
}