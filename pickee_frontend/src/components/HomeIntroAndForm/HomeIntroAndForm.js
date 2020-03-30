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
    created: function() {
        // On the page load - check url parameters and
        // change screen if it is ?step=2
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        const step = urlParams.get('step')
        if (step && step == 2) {
            this.isFormHidden = false;
            this.isFormActive = true;
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