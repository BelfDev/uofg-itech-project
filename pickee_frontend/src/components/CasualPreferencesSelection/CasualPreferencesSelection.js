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
            genreValue: '',
            iconPlay: mdiPlayCircleOutline,
            token: this.$cookies.get("csrftoken")
        }
    },
    props: ['user'],
    methods: {
        updateGenreValue: function(values) {
            this.genreValue = values.map(v => {
                const matchIndex = this.items.findIndex(k => k.text === v);
                return this.items[matchIndex].value;
            }).join(',');
        }
    },
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