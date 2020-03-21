<template>
    <v-app>
        <div class="page-home">
            <v-content>
                <HomeIntroAndForm :data="data" />
            </v-content>
        </div>
    </v-app>
</template>

<script>
    import HomeIntroAndForm from '@/components/HomeIntroAndForm/HomeIntroAndForm.vue';

    export default {
        name: "Home",
        data: () => ({
            data: {}
        }),
        methods: {},
        components: {
            HomeIntroAndForm
        },
        beforeMount() {
            const appElement = document.getElementsByTagName('app')[0];
            const data = appElement.getAttribute('data');
            if (data) {
                this.data = JSON.parse(data);
            }
        }
    };
</script>
