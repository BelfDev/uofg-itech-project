import PageHeader from '@/components/PageHeader/PageHeader.vue';
import Intro from '@/components/Intro/Intro.vue';
import CasualPreferencesSelection from '@/components/CasualPreferencesSelection/CasualPreferencesSelection.vue';

export default {
    name: 'HomeIntroAndForm',
    methods: {
        showFormScreen: function() {
            this.isFormActive = !this.isFormActive;
        }
    },
    data: () => ({
        isFormActive: false
    }),
    components: {
        PageHeader,
        Intro,
        CasualPreferencesSelection
    }
}