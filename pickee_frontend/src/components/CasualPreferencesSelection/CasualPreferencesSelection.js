import TimeSlider from "@/components/TimeSlider/TimeSlider.vue";

export default {
    name: 'CasualPreferencesSelection',
    data: () => ({
        select: ["Action", "Fantasy"],
        items: ["Action", "Drama", "Fantasy", "Sci-Fi"],
    }),
    components: {
        TimeSlider
    }
}