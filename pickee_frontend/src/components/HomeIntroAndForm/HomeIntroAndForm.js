import PageHeader from '@/components/PageHeader/PageHeader.vue';
import Intro from '@/components/Intro/Intro.vue';
import CasualPreferencesSelection from '@/components/CasualPreferencesSelection/CasualPreferencesSelection.vue';

export default {
    name: 'HomeIntroAndForm',
    methods: {
        showFormScreen: function() {
            this.isFormHidden = false;

            setTimeout(() => {
                this.isFormActive = !this.isFormActive;
            }, 300);
        }
    },
    props: ['data'],
    data: () => ({
        isFormHidden: true,
        isFormActive: false
    }),
    components: {
        PageHeader,
        Intro,
        CasualPreferencesSelection
    }
}