import TimeSlider from "@/components/TimeSlider/TimeSlider.vue";
import SessionUserSelector from "@/components/SessionUserSelector/SessionUserSelector.vue";
import api from "@/services/api";
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
        const response = await api.getGenres();
        this.items = response.map(item => ({
            text: item.name,
            value: item.id
        }));
    },
    components: {
        TimeSlider,
        SessionUserSelector
    }
}